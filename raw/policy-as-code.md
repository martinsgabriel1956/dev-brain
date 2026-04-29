---
date: 2026-04-23
tags: [tech-mentor, security, devsecops, policy-as-code]
skill: tech-mentor-security/references/policy-as-code
level: intermediário
---

# Policy as Code

## Contexto

Policies de segurança definidas em documentos ou wikis quebram silenciosamente — ninguém as lê, ninguém as enforça, e o drift entre o que está escrito e o que está rodando é inevitável. Policy as Code transforma regras de compliance e segurança em artefatos versionados, testáveis e executados automaticamente no pipeline ou no cluster.

É a extensão natural do DevSecOps: assim como infraestrutura virou código com Terraform, policies viram código com OPA/Rego.

## Como Funciona

**Open Policy Agent (OPA)** é o engine de avaliação de policies. Recebe um input (JSON com contexto), avalia contra uma policy escrita em **Rego** e retorna uma decisão (`allow`, `deny`, ou dados customizados).

```
Input (request/resource) → OPA engine + Rego policy → Decision
```

**Pontos de integração:**

| Ferramenta | Onde atua | Como |
|---|---|---|
| **Conftest** | CI pipeline | Valida arquivos YAML/JSON/Terraform contra policies Rego |
| **Kyverno** | Kubernetes admission | Controller nativo K8s, policies em YAML |
| **OPA Gatekeeper** | Kubernetes admission | OPA como admission webhook, policies em Rego |
| **Styra DAS** | Centralizado | Gestão de policies OPA em escala |

### Rego — Sintaxe Básica

```rego
# policy/deny-latest-tag.rego
package main

# Nega deployments com imagem usando tag "latest"
deny[msg] {
  input.kind == "Deployment"
  container := input.spec.template.spec.containers[_]
  endswith(container.image, ":latest")
  msg := sprintf("Container '%v' usa tag :latest — proibido em produção", [container.name])
}
```

```bash
# Testando no CI com Conftest
conftest test deployment.yaml --policy policy/
```

### Kyverno — Policy em YAML

```yaml
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: disallow-latest-tag
spec:
  validationFailureAction: Enforce
  rules:
    - name: check-image-tag
      match:
        resources:
          kinds: [Deployment]
      validate:
        message: "Imagem deve ter tag explícita, não :latest"
        pattern:
          spec:
            template:
              spec:
                containers:
                  - image: "!*:latest"
```

### OPA Gatekeeper — ConstraintTemplate

```yaml
# Define o tipo de constraint
apiVersion: templates.gatekeeper.sh/v1
kind: ConstraintTemplate
metadata:
  name: k8srequiredlabels
spec:
  crd:
    spec:
      names:
        kind: K8sRequiredLabels
  targets:
    - target: admission.k8s.gatekeeper.sh
      rego: |
        package k8srequiredlabels
        violation[{"msg": msg}] {
          provided := {label | input.review.object.metadata.labels[label]}
          required := {"owner", "team"}
          missing := required - provided
          count(missing) > 0
          msg := sprintf("Labels obrigatórias ausentes: %v", [missing])
        }
```

### Pipeline CI com Conftest

```yaml
# .github/workflows/security.yml
- name: Policy check (Conftest)
  run: |
    conftest test k8s/ --policy policies/ --all-namespaces
    conftest test terraform/ --policy policies/terraform/
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Versionamento | Policies no git com PR review | Curva de aprendizado do Rego |
| Enforcement | Bloqueio automático antes do deploy | False positives podem frear times |
| Testabilidade | `opa test` para unit tests de policies | Testes de policy precisam de manutenção |
| Kyverno vs OPA | Kyverno é mais simples (YAML nativo) | OPA é mais flexível para casos complexos |
| Audit mode | Detecta violations sem bloquear (warn) | Equipes podem ignorar warnings por tempo |

## Quando Usar / Quando Evitar

**Usar quando:**
- Compliance requer evidência de enforcement automático (SOC 2, PCI)
- Times grandes onde drift de configuração é frequente
- Multi-tenant Kubernetes com isolamento entre times
- Qualquer regra que hoje é "por favor seguir o runbook"

**Evitar quando:**
- Time pequeno com cultura forte de revisão manual — overhead não compensa
- Policies muito dinâmicas que mudam semanalmente — manutenção vira fardo

**Sequência recomendada:**
1. Começar com `audit` mode (warn, não block)
2. Validar false positive rate por 2 semanas
3. Mudar para `enforce` mode
4. Adicionar `opa test` no CI das próprias policies

## Conceitos Relacionados

[[devsecops-pipeline]] · [[kubernetes-security]] · [[cloud-security]] · [[compliance-soc2-pci]] · [[supply-chain-security]]

---
*Fonte: tech-mentor skill · tech-mentor-security · 2026-04-23*
