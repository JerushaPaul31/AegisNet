# AegisNet

AI-powered telecom threat intelligence platform for detecting fake cell towers (IMSI Catchers) and SMS phishing attacks (SMS Blasters).

## The Problem

Threats such as IMSI catchers and SMS blasters can exploit mobile communication systems by impersonating legitimate cell towers. These rogue towers can broadcast strong signals that attract nearby devices and, in some attack scenarios, force a downgrade to older network technologies such as 2G, where weaker security mechanisms can be exploited.

Once connected, users may be exposed to malicious activity such as interception attempts and large-scale phishing or
scam SMS campaigns.
Because these attacks occur at the network level, they can potentially affect multiple users within the same geographic area.

## Our Solution 
We built **AegisNet**, an AI-powered telecom threat intelligence platform designed to detect and correlate
these threats. AegisNet analyzes network telemetry such as signal strength, network transitions, cell/tower identifiers, and other available device measurements, alongside suspicious SMS patterns. These signals are combined across multiple devices to identify potential rogue-tower and coordinated phishing incidents.

The result is a centralized threat intelligence system that can provide operators with real-time visibility into
potential attacks.

## Core Features
- Telecom signal anomaly detection
- Rogue tower / IMSI catcher detection
- SMS phishing detection
- AI-based threat analysis
- Multi-device threat correlation
- Threat scoring and visualization
- Operator threat dashboard
- Device reporting

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- React
- Machine Learning
- NLP
- Docker

## Status

🚧 Under development