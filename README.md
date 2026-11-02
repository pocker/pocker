# Hi, I'm David 👋

**Lead Software Engineer** · 12+ years · Hungary

Backend, cloud and CI/CD engineer with a habit of going down to the firmware and driver level when a problem calls for it.

<p>
  <img src="https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white" />
  <img src="https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=cplusplus&logoColor=white" />
  <img src="https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=springboot&logoColor=white" />
  <img src="https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB" />
  <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white" />
  <img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white" />
  <img src="https://img.shields.io/badge/ESP32-E7352C?style=flat-square&logo=espressif&logoColor=white" />
</p>

## About

I have built software for healthcare research, national eHealth infrastructure, IoT and smart home platforms, a real-time multiplayer games platform, and large-scale e-commerce checkout. I currently lead engineering work on a checkout platform and manage a team of five.

- Took part in two monolith-to-microservice migrations, as a contributor on one and a key engineer on the other.
- Owned CI/CD, cloud deployment and production readiness for a high-traffic service.
- Contributed Bluetooth LE support to Wine/Proton. It is merged upstream and shipped in GE-Proton.
- Build AI-assisted development workflows with Claude Code: multi-agent pipelines that plan, implement, review and test changes, plus agent context and skills for large codebases.

## Experience

**Checkout platform, global online travel company** · *2020 – present*
Key engineer in extracting checkout from a legacy web monolith into a standalone Java/Kotlin Spring Boot service. The service covers flights, hotels, cars, packages, cruises and activities across multiple brands and markets.
- Designed CI/CD on GitHub Actions and Spinnaker, with a Kubernetes environment for every PR and Cypress end-to-end tests
- Replaced long-lived CI credentials with GitHub OIDC; added CodeQL scanning and moved artifact publishing to Artifactory
- Migrated tracing to OpenTelemetry and Datadog; tuned startup time, resource limits and autoscaling
- Mentoring, planning, and technical design for new components

**Real-time multiplayer games framework** · *2019 – 2020* · Architect & lead developer
Designed a greenfield framework for web-based multiplayer games on top of an automatic scoring hardware system. I chose the stack, defined the coding standards, led the team and acted as Scrum Master.
*NestJS · React · React Native · Socket.io · TypeScript*

**Smart home and alarm platform** · *2017 – 2019* · Lead developer
Moved device-to-server communication from raw sockets to AWS IoT with a certificate per device. Added Z-Wave support, rule-based automations, WebSocket messaging, a cross-platform mobile app and IP camera streaming. Contributed to the migration from the monolith to microservices.
*Spring Boot · Python · AWS IoT / Lambda / SNS · Ionic · PostgreSQL*

**Earlier** · *2014 – 2020*
Greenhouse monitoring tools, national eHealth infrastructure (Liferay, WildFly, SOAP, SAML), and university healthcare research pilots: stroke rehabilitation, heart-rate monitoring and a portable plethysmograph (Android NDK, C++).

## Open source

- **[GE-Proton #817](https://github.com/GloriousEggroll/proton-ge-custom/pull/817)** (merged): opt-in Bluetooth LE support in Wine/Proton. Zwift and Rouvy can now pair directly with smart trainers on Linux.
- **[BikeControl #424](https://github.com/OpenBikeControl/bikecontrol/pull/424)**: Linux desktop support for the open-source controller and virtual-shifting app (Flutter).
- **[pocker/wine](https://github.com/pocker/wine)**: Wine fork with the BLE implementation (`winebth.sys`, `bluetoothapis`, WinRT `Windows.Devices.Bluetooth`).

## Projects

- **Grupetto**: organise group rides and runs with your club, including events, live tracking, routes and race results. *Launching soon.*<br/>
  <sub>Python · React · React Native</sub>
- **[fsi6-joystick](https://github.com/pocker/fsi6-joystick)**: turns a FlySky iBUS/SBUS receiver into a Linux joystick for FPV simulators.<br/>
  <sub>Python · uinput</sub>
- **Hardware and firmware**: a BLE power-driven fan controller, an ESP-NOW floor heating controller with Home Assistant integration, a 3D printer multi-material unit with a [Klipper plugin](https://github.com/pocker/chamois-klipper), and a [custom relay board](https://github.com/pocker/oli-relay-controller).<br/>
  <sub>ESP32 · C++ · PlatformIO · ESPHome · PCB design</sub>

## Toolbox

| | |
|---|---|
| **Languages** | Java · Kotlin · TypeScript / JavaScript · Python · C / C++ |
| **Backend** | Spring Boot · Node.js / NestJS · FastAPI · gRPC · GraphQL · REST |
| **Frontend & mobile** | React · React Native · Ionic |
| **Cloud & DevOps** | AWS · Docker · Kubernetes · Helm · GitHub Actions · Spinnaker · Jenkins |
| **Observability** | OpenTelemetry · Datadog · Splunk · Grafana |
| **Testing** | JUnit 5 · TestNG · Mockito · Cypress · Jest · Vitest · pytest |
| **Data** | PostgreSQL · MongoDB · Redis · Elasticsearch |
| **Embedded** | ESP32 · PlatformIO · ESPHome · BLE · MQTT · Z-Wave |
