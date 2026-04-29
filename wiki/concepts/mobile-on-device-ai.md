---
type: concept
title: "On-Device AI — Mobile"
aliases: ["core ml ios", "tflite android", "mediapipe mobile", "gemini nano on device"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_count: 1
tags: [mobile, on-device-ai, coreml, tflite, mediapipe, gemini-nano, quantization]
skill: tech-mentor-mobile
status: stable
---

# On-Device AI — Mobile

Inferência local: privacidade, latência zero, funciona offline, sem custo de API.

## iOS — Core ML

```swift
let model = try MLModel(contentsOf: modelURL)
let request = VNCoreMLRequest(model: VNCoreMLModel(for: model))
let handler = VNImageRequestHandler(ciImage: ciImage)
try handler.perform([request])
let results = request.results as? [VNClassificationObservation]
```

Neural Engine em iPhones A12+ — inferência sem consumir CPU/GPU. `coremltools` converte PyTorch/TensorFlow para `.mlmodel`.

## Android — TFLite / LiteRT

```kotlin
val interpreter = Interpreter(loadModelFile("model.tflite"))
val input = Array(1) { FloatArray(224 * 224 * 3) }
val output = Array(1) { FloatArray(1000) }
interpreter.run(input, output)
```

INT8 quantização: 4x menor, 2-4x mais rápido, precisão ~1% menor. NNAPI para aceleração de hardware.

## MediaPipe Tasks

```ts
// Cross-platform — RN, Flutter, web
const imageClassifier = await ImageClassifier.createFromOptions({
    baseOptions: { modelAssetPath: 'classifier.tflite' },
    maxResults: 5,
});
const result = imageClassifier.classify(image);
```

Modelos pré-treinados para: classificação, detecção de objetos, pose estimation, NLP.

## Gemini Nano (Android 14+)

```kotlin
val generativeModel = GenerativeModel(modelName = "gemini-nano")
val response = generativeModel.generateContent("Resumir: $text")
```

Requer AICore — disponível em Pixel 8+, Samsung S24+. Verificar disponibilidade antes de usar.

## Trade-offs

| Critério | On-Device | Cloud API |
|---|---|---|
| Privacidade | ✅ | ❌ |
| Latência | ✅ (~10ms) | ❌ (~200ms+) |
| Funciona offline | ✅ | ❌ |
| Modelos complexos | ❌ | ✅ |
| Custo | ✅ (zero por request) | ❌ |

## Ver também

- [[mobile-profiling]] — medir impacto de inferência no FPS
- [[como-llms-funcionam]] — como modelos funcionam internamente

## Key Sources

- [[wiki/sources/mobile-on-device-ai]]
