---
title: "Computer Communication Networks"
full_name: "COMP4621 Computer Communication Networks"
type: source
tags: [courses, comp, undergraduate, computer-networks, protocols, distributed-systems, comp4621, level-4]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/COMP/COMP4621"
confidence: medium
---

## 概述

COMP4621 計算機通信網絡為計算機科學四年級學生提供互聯網協議棧的完整系統訓練，以 Kurose & Ross《計算機網絡：自頂向下方法》（第八版）為標準教材，先修要求為 COMP3511 操作系統，了解 C 語言套接字程式設計尤為有利。課程採用自頂向下架構，從學生熟悉的應用層協議（HTTP/2、DNS、SMTP）出發，逐層深入傳輸層（TCP 的可靠傳輸狀態機、AIMD 擁塞控制、CUBIC/BBR）、網路層（IP 尋址、CIDR、Dijkstra 鏈路狀態與 Bellman-Ford 距離向量路由、BGP 域間路由）及鏈路層（Ethernet、WiFi CSMA/CA、ARP），最終觸及物理層的 Shannon 通道容量定理。軟體定義網絡（SDN）章節介紹控制平面與資料平面分離的現代設計範式。學生完成課程後能夠分析端到端網絡延遲（傳輸延遲＋傳播延遲＋排隊延遲）、以套接字 API 實現 TCP/UDP 網絡應用、理解 TLS 握手與 HTTPS 的安全機制，並運用 Little's Law 分析網絡隊列性能。計算機網絡是雲端基礎設施、分佈式系統、CDN 設計及網絡安全工程的技術根基。

## Course Overview

**Textbook**: Kurose & Ross, *Computer Networking: A Top-Down Approach*

Structured top-down: starts with application-layer protocols familiar to students, then descends through transport, network, link, and physical layers.

## Key Topics

### Application Layer
- **HTTP/HTTPS**: request-response; stateless; persistent vs. non-persistent connections; HTTP/2 multiplexing
- **DNS**: hierarchical name space; resource records (A, AAAA, CNAME, MX); resolver process; caching
- **SMTP/IMAP/POP**: email protocols; MIME; DKIM for authentication
- **P2P**: BitTorrent; DHT (Distributed Hash Table); content distribution networks (CDNs)
- **Socket programming**: TCP and UDP sockets; client-server model

### Transport Layer
- **UDP**: unreliable, connectionless; checksum only; used in DNS, streaming, VoIP
- **TCP**: reliable, connection-oriented; three-way handshake; sequence numbers; ACKs
- **Reliable data transfer**: rdt 1.0, 2.0, 3.0 state machines; stop-and-wait; pipelining
- **Go-Back-N and Selective Repeat**: sliding window protocols
- **TCP congestion control**: slow start; AIMD (additive increase, multiplicative decrease); congestion avoidance; fast recovery; CUBIC, BBR
- **TCP flow control**: receive window (rwnd); sender limited by min(cwnd, rwnd)
- **Multiplexing**: port numbers; ephemeral ports; well-known ports (80, 443, 22)

### Network Layer
- **IP addressing**: IPv4 (32-bit), IPv6 (128-bit); CIDR; subnetting; NAT
- **Packet forwarding**: longest prefix matching; forwarding table vs. routing table
- **ICMP**: ping, traceroute; error reporting
- **Routing algorithms**:
  - **Link-state** (Dijkstra): Ospf; global view; $O(n^2)$ complexity
  - **Distance-vector** (Bellman-Ford): RIP; distributed; count-to-infinity problem
  - **BGP**: inter-AS routing; path attributes; hot potato routing
- **SDN**: control plane decoupled from data plane; OpenFlow; match-action tables

### Link Layer
- **Error detection**: parity; CRC; checksum
- **Multiple access protocols**: TDMA, FDMA; CSMA/CD (Ethernet); CSMA/CA (WiFi); ALOHA
- **Ethernet**: MAC addresses; ARP; switches vs. hubs; VLAN
- **WiFi (802.11)**: SSID; BSS; association; 802.11ac/ax (WiFi 5/6); OFDM

### Physical Layer
- Encoding: NRZ, Manchester; baud rate vs. bit rate
- Transmission media: copper (twisted pair, coax), fiber, wireless
- Shannon capacity: $C = B \log_2(1 + S/N)$; Nyquist theorem

### Performance and Queuing
- **Transmission delay**: $L/R$; propagation delay: $d/c$; queuing delay; processing delay
- Bandwidth-delay product: amount of data "in flight"
- Little's Law at network queues: $L = \lambda W$ — see [[littles-law]]
- Throughput bottlenecks; end-to-end delay calculation

## Related Concepts

- [[web-architecture]]
- [[cryptography]]
- [[database-systems]]
- [[littles-law]]

## Source Materials

- COMP4621 Course Materials
