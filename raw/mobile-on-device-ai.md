---
date: 2026-04-23
tags: [tech-mentor, mobile, ai, on-device, core-ml, tflite, mediapipe, gemini-nano, edge-ai]
skill: tech-mentor-mobile/references/ia
level: arquiteto
---

# On-Device AI — Core ML, TFLite, MediaPipe, Gemini Nano

## Contexto
On-device AI processa modelos diretamente no device, sem chamada de rede. Os benefícios são latência zero, privacidade (dados não saem do device), e funcionamento offline. O custo é tamanho do app (+50MB–500MB), consumo de bateria e limitações de modelos disponíveis. A decisão entre on-device e API é um trade-off arquitetural com implicações de produto.

## Como Funciona

### Quando processar no edge vs API

```
On-device:
✓ Privacidade crítica (documento de identidade, dados biométricos, saúde)
✓ Latência < 100ms obrigatória (realidade aumentada, câmera em tempo real)
✓ Funcionalidade offline essencial
✓ Modelo pequeno (< 50MB quantizado)
✓ Inferência frequente (cada frame da câmera)

API:
✓ Modelo grande (GPT-4, Claude, Gemini Pro) — não cabe no device
✓ Acurácia máxima mais importante que latência
✓ Modelo atualizado frequentemente sem release de app
✓ Uso esporádico (não compensa carregar modelo em memória)
✓ Recursos do device limitados (target de devices low-end)
```

### iOS — Core ML

```swift
import CoreML
import Vision
import CoreImage

// Classificação de imagem com Vision + Core ML
class ImageClassifier {
  private var model: VNCoreMLModel?

  func loadModel() throws {
    // Modelo compilado (.mlmodelc) incluído no bundle
    let config = MLModelConfiguration()
    config.computeUnits = .all // CPU + GPU + Neural Engine

    let mlModel = try MobileNetV2(configuration: config)
    model = try VNCoreMLModel(for: mlModel.model)
  }

  func classify(image: UIImage) async throws -> [(label: String, confidence: Float)] {
    guard let model = model, let cgImage = image.cgImage else { return [] }

    return try await withCheckedThrowingContinuation { continuation in
      let request = VNCoreMLRequest(model: model) { request, error in
        if let error { continuation.resume(throwing: error); return }

        let results = request.results as? [VNClassificationObservation] ?? []
        let top5 = results.prefix(5).map { (label: $0.identifier, confidence: $0.confidence) }
        continuation.resume(returning: top5)
      }

      request.imageCropAndScaleOption = .centerCrop

      let handler = VNImageRequestHandler(cgImage: cgImage, options: [:])
      try? handler.perform([request])
    }
  }
}

// Detecção de face em tempo real (câmera)
class FaceDetector {
  private let sequenceHandler = VNSequenceRequestHandler()

  func detectFaces(in pixelBuffer: CVPixelBuffer) throws -> [VNFaceObservation] {
    let request = VNDetectFaceRectanglesRequest()
    try sequenceHandler.perform([request], on: pixelBuffer, orientation: .up)
    return request.results ?? []
  }
}

// Core ML com modelo custom (exportado do Python)
// python: coremltools.convert(model, inputs=[...]).save("MyModel.mlpackage")
class CustomModel {
  private let model = try! MyModel(configuration: MLModelConfiguration())

  func predict(input: MLMultiArray) -> Float {
    let prediction = try? model.prediction(input: input)
    return prediction?.output.floatValue ?? 0
  }
}
```

### Android — TensorFlow Lite (TFLite)

```kotlin
// build.gradle.kts
dependencies {
  implementation("org.tensorflow:tensorflow-lite:2.14.0")
  implementation("org.tensorflow:tensorflow-lite-gpu:2.14.0") // GPU delegate
  implementation("org.tensorflow:tensorflow-lite-task-vision:0.4.4") // API de alto nível
}
```

```kotlin
// Classificação de imagem com TFLite Task API
import org.tensorflow.lite.task.vision.classifier.ImageClassifier

class ImageClassifierManager(private val context: Context) {
  private lateinit var classifier: ImageClassifier

  fun initialize() {
    val options = ImageClassifier.ImageClassifierOptions.builder()
      .setBaseOptions(
        BaseOptions.builder()
          .setNumThreads(4)
          .useGpu() // delegação para GPU
          .build()
      )
      .setMaxResults(5)
      .setScoreThreshold(0.3f)
      .build()

    // Modelo .tflite na pasta assets/
    classifier = ImageClassifier.createFromFileAndOptions(
      context,
      "mobilenet_v2.tflite",
      options
    )
  }

  fun classify(bitmap: Bitmap): List<Classifications> {
    val image = TensorImage.fromBitmap(bitmap)
    return classifier.classify(image)
  }

  fun close() = classifier.close()
}

// Inferência de texto — SentenceEncoder
class TextEmbedder(context: Context) {
  private val embedder = TextEmbedder.createFromFile(context, "universal_sentence_encoder.tflite")

  fun embed(text: String): FloatArray {
    val result = embedder.embed(text)
    return result.embeddingByIndex(0).floatArray()
  }

  fun similarity(text1: String, text2: String): Float {
    val emb1 = embed(text1)
    val emb2 = embed(text2)
    return cosineSimilarity(emb1, emb2)
  }

  private fun cosineSimilarity(a: FloatArray, b: FloatArray): Float {
    val dot = a.zip(b).sumOf { (x, y) -> (x * y).toDouble() }.toFloat()
    val normA = Math.sqrt(a.sumOf { (it * it).toDouble() }).toFloat()
    val normB = Math.sqrt(b.sumOf { (it * it).toDouble() }).toFloat()
    return dot / (normA * normB)
  }
}
```

### MediaPipe — Tasks de alto nível

MediaPipe oferece soluções prontas para visão, linguagem e áudio — sem precisar treinar ou adaptar modelos.

```kotlin
// Android — MediaPipe Tasks
// build.gradle: implementation("com.google.mediapipe:tasks-vision:0.10.x")

class HandTracker(context: Context) {
  private val handLandmarker: HandLandmarker

  init {
    val options = HandLandmarker.HandLandmarkerOptions.builder()
      .setBaseOptions(BaseOptions.builder().setModelAssetPath("hand_landmarker.task").build())
      .setNumHands(2)
      .setMinHandDetectionConfidence(0.5f)
      .setMinTrackingConfidence(0.5f)
      .setRunningMode(RunningMode.LIVE_STREAM)
      .setResultListener { result, _ ->
        // 21 landmarks por mão, em tempo real
        result.landmarks().forEach { handLandmarks ->
          val landmarks = handLandmarks.map { Point(it.x(), it.y(), it.z()) }
          processHandGesture(landmarks)
        }
      }
      .build()

    handLandmarker = HandLandmarker.createFromOptions(context, options)
  }
}
```

```swift
// iOS — MediaPipe Tasks Swift
// Swift Package: com.google.mediapipe.MediaPipeTasksVision

import MediaPipeTasksVision

class ObjectDetector {
  private var detector: ObjectDetector!

  func setup() throws {
    let options = ObjectDetectorOptions()
    options.baseOptions.modelAssetPath = Bundle.main.path(forResource: "efficientdet", ofType: "tflite")!
    options.runningMode = .liveStream
    options.maxResults = 5
    options.scoreThreshold = 0.5
    options.objectDetectorLiveStreamDelegate = self
    detector = try ObjectDetector(options: options)
  }

  func detect(sampleBuffer: CMSampleBuffer, orientation: UIImage.Orientation) {
    let image = try? MPImage(sampleBuffer: sampleBuffer, orientation: orientation)
    try? detector.detectAsync(image: image!, timestampInMilliseconds: Int(Date().timeIntervalSince1970 * 1000))
  }
}
```

### Gemini Nano — LLM on-device (Android 14+)

```kotlin
// Disponível via AICore API (Android 14+, Pixel 8+)
// Modelos maiores via API Gemini

import com.google.ai.client.generativeai.GenerativeModel
import com.google.ai.client.generativeai.type.generationConfig

class OnDeviceLLM {
  // Gemini Nano — on-device (quando disponível)
  private val onDeviceModel = GenerativeModel(
    modelName = "gemini-nano",
    generationConfig = generationConfig {
      maxOutputTokens = 256
      temperature = 0.7f
    }
  )

  suspend fun summarize(text: String): String? {
    return try {
      val response = onDeviceModel.generateContent("Resuma em uma frase: $text")
      response.text
    } catch (e: Exception) {
      // Fallback para API se on-device não disponível
      null
    }
  }
}
```

### React Native — Integração com modelos

```typescript
// react-native-fast-tflite
import { TensorflowModel, useTensorflowModel } from "react-native-fast-tflite";

export function ImageClassifierView() {
  const model = useTensorflowModel(require("./assets/model.tflite"));

  async function classifyImage(imageUri: string) {
    if (!model || model.state !== "loaded") return;

    // Pré-processar imagem
    const input = await preprocessImage(imageUri, { width: 224, height: 224 });

    // Inferência — roda na thread nativa (não bloqueia JS)
    const output = model.runSync([input]);

    return interpretOutput(output[0]);
  }

  return <CameraView onCapture={classifyImage} />;
}
```

## Trade-offs

| Solução | Tamanho do modelo | Latência | Privacidade | Setup | Ideal para |
|---|---|---|---|---|---|
| Core ML | Variável | < 5ms (Neural Engine) | Total | Médio | iOS, modelos Apple-otimizados |
| TFLite | 1–50MB | 10–100ms | Total | Baixo | Android, cross-platform |
| MediaPipe | 1–30MB | < 10ms | Total | Muito baixo | Visão/áudio, tarefas comuns |
| Gemini Nano | ~1.8GB | 50–200ms | Total | Nenhum (sistema) | Texto, sumarização (Pixel 8+) |
| API Gemini/GPT | Nenhum | 500ms–5s | Dados saem do device | Baixo | Modelos grandes, acurácia máxima |

## Quando Usar / Quando Evitar

**On-device obrigatório:** câmera em tempo real (AR, filtros), privacidade regulada (HIPAA, dados biométricos), funcionalidade offline core.

**API obrigatória:** modelos > 100MB, inferência esporádica, acurácia como prioridade absoluta.

**MediaPipe first:** para detecção facial, pose, mão, segmentação de imagem — já está otimizado e testado. Não reimplemente.

**Quantização:** sempre quantize modelos para INT8 antes de incluir no app — reduz tamanho 4x com queda de acurácia < 1% na maioria dos casos.

## Conceitos Relacionados
[[mobile-performance-listas]] · [[mobile-metricas-criticas]] · [[mobile-cross-platform-decision]] · [[como-llms-funcionam]]

---
*Fonte: tech-mentor skill · tech-mentor-mobile · 2026-04-23*
