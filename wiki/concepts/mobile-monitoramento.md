---
type: concept
title: "Monitoramento Mobile"
aliases: ["mobile crashlytics", "mobile sentry", "mobile observability", "mobile performance monitoring"]
date_created: 2026-04-24
date_updated: 2026-04-24
source_count: 1
tags: [mobile, monitoramento, crashlytics, sentry, performance-monitoring, alertas]
skill: tech-mentor-mobile
status: stable
---

# Monitoramento Mobile

## Stack Recomendada

- **Crash reporting:** Firebase Crashlytics (gratuito) ou Sentry (session replay)
- **Performance:** Firebase Performance Monitoring (startup, network)
- **Analytics:** Firebase Analytics ou Mixpanel
- **Alertas:** Firebase Alerts ou PagerDuty integrado ao Crashlytics

## Firebase Crashlytics

```ts
// React Native
crashlytics().setUserId(user.id);
crashlytics().setAttribute('plan', user.plan);

try {
    await riskyOperation();
} catch (error) {
    crashlytics().recordError(error);
    throw error;
}
```

Symbolication automática — stack trace legível sem upload manual. Agrupa crashes por root cause.

## Sentry

```ts
Sentry.init({
    dsn: 'https://xxx@sentry.io/yyy',
    tracesSampleRate: 0.2,
    enableAutoSessionTracking: true,
});

Sentry.setUser({ id: user.id, email: user.email });
```

Session replay captura taps e telas antes do crash — reduz MTTR.

## Alertas Obrigatórios

- Crash-free rate < 99.5%
- ANR rate > 0.1%
- Cold start p95 > 3s
- Network error rate > 2%

## Structured Logging

```ts
logger.error({
    message: 'payment_failed',
    userId: user.id,
    sessionId: session.id,
    errorCode: error.code,
});
```

userId + sessionId permitem correlacionar crashlytics com logs de servidor.

## Ver também

- [[mobile-metricas-criticas]] — o que monitorar
- [[mobile-cicd]] — gates de qualidade antes de cada deploy
- [[observabilidade]] — princípios gerais de observabilidade

## Key Sources

- [[wiki/sources/mobile-monitoramento]]
