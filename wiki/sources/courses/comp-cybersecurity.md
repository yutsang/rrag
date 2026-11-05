---
title: "Cybersecurity"
full_name: "COMP3632 Principles of Cybersecurity"
type: source
tags: [courses, comp, undergraduate, cybersecurity, cryptography, network-security, comp3632, level-3]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/COMP/COMP3632"
confidence: medium
---

## 概述

COMP3632 網絡安全原理為計算機科學三年級學生系統介紹現代信息安全的攻防兩端，以 CIA 三元組（機密性、完整性、可用性）為核心框架，先修要求為 COMP2012 及 COMP3511 操作系統，具備 C/C++ 底層程式設計基礎尤為重要。課程涵蓋對稱加密（AES、串流密碼）與非對稱加密（RSA、Diffie-Hellman 金鑰交換、橢圓曲線密碼學）的數學基礎、雜湊函數與數位簽章、PKI 憑證體系、TLS/SSL 握手協議、網路防火牆與 IDS/IPS，以及 OWASP Top 10 中的 SQL 注入、XSS、CSRF 等 Web 應用漏洞的原理與防禦。系統安全部分深入堆疊緩衝區溢位攻擊與 ASLR、DEP 等現代防護機制，並介紹滲透測試的標準方法論。學生完成課程後能夠辨識常見攻擊向量、分析惡意軟件行為（靜態與動態分析）、設計安全的加密通信系統，以及評估組織的安全態勢。資訊安全是數字商業基礎設施、金融科技（區塊鏈智能合約安全）及電子政務的關鍵保障，使本課程在工程實踐中具有高度實用價值。

## Key Topics

### Security Foundations
- **CIA Triad**: Confidentiality, Integrity, Availability
- Security vs. usability trade-off; threat modeling; attack surface analysis
- Authentication, authorization, accounting (AAA framework)
- Security policies; access control models: DAC, MAC, RBAC

### Cryptography
- **Symmetric encryption**: stream ciphers (RC4, ChaCha20); block ciphers (AES, DES/3DES)
  - Modes of operation: ECB, CBC, CTR, GCM (authenticated encryption)
  - Key distribution problem
- **Asymmetric (public-key) encryption**: RSA; Diffie-Hellman key exchange
  - RSA: $c = m^e \mod n$; $m = c^d \mod n$; security based on integer factorization
  - DH: discrete logarithm problem; ECDH (elliptic curve variant)
- **Hash functions**: SHA-256, SHA-3; properties (preimage, second preimage, collision resistance)
- **MACs and digital signatures**: HMAC; RSA/ECDSA signatures; non-repudiation
- **PKI**: certificates (X.509); certificate authorities; trust chains; revocation (CRL, OCSP)
- See [[cryptography]]

### Network Security
- **TLS/SSL**: handshake protocol; certificate verification; HSTS; cipher suites
- **Firewalls**: packet filtering; stateful inspection; application layer (proxy)
- **IDS/IPS**: signature-based vs. anomaly-based; false positive/negative trade-off
- **VPN**: tunneling protocols (IPSec, OpenVPN, WireGuard); split tunneling
- Common attacks:
  - **DoS/DDoS**: volumetric, protocol, application layer; mitigation (rate limiting, CDN)
  - **Man-in-the-middle**: ARP spoofing; SSL stripping; DNSSEC defense
  - **DNS attacks**: cache poisoning; DNSSEC; DoH/DoT

### Web Application Security (OWASP Top 10 highlights)
- **SQL Injection**: malicious SQL in user input; parameterized queries as defense
- **Cross-Site Scripting (XSS)**: reflected, stored, DOM-based; CSP headers as mitigation
- **Cross-Site Request Forgery (CSRF)**: anti-CSRF tokens; SameSite cookies
- **Authentication vulnerabilities**: weak passwords; credential stuffing; MFA
- **Insecure Direct Object References**: access control failures; principle of least privilege
- **Security misconfiguration**: default credentials; exposed admin interfaces

### System Security
- **Buffer overflow**: stack smashing; return-address overwrite; shellcode injection
  - Defenses: ASLR, DEP/NX, stack canaries, control-flow integrity (CFI)
- **Privilege escalation**: SUID/SGID abuse; kernel exploits; container escapes
- **Malware taxonomy**: virus, worm, trojan, ransomware, rootkit, spyware
- Reverse engineering intro: static analysis (strings, disassembly); dynamic analysis (sandboxing)

### Security Management
- Penetration testing methodology: reconnaissance, scanning, exploitation, post-exploitation, reporting
- Vulnerability disclosure: responsible vs. full disclosure; CVE system
- Incident response: containment, eradication, recovery; forensics preservation

## Related Concepts

- [[cryptography]]
- [[web-architecture]]
- [[algorithms-and-data-structures]]

## Source Materials

- COMP3632 Course Materials
