# 🛰️ Steampipe MCP Server

This project is a prototype MCP (Model Context Protocol) server designed to interface with [Steampipe](https://steampipe.io) and AWS. It enables users to query AWS cloud resources using natural language — without needing to understand AWS-specific terminology or write raw SQL.

---

## 🚀 Purpose

The goal of this project is to **bridge the gap** between cloud complexity and human-friendly queries. By integrating Steampipe with MCP, this server allows developers, analysts, and even non-technical users to ask questions like:

- "How many EC2 instances are running?"
- "Which S3 buckets are publicly accessible?"
- "What was the highest AWS cost last month?"
- "Do any IAM users have administrator access?"

…and automatically receive structured responses pulled from your AWS environment.

---

## ✨ Features

- ✅ **Natural Language Interface**: Accepts plain English questions.
- 🔄 **Dynamic SQL Generation**: Translates input into Steampipe SQL queries.
- 🔍 **AWS Resource Insight**: Query EC2, S3, IAM, CloudTrail, and more.
- 💸 **Cost & Usage Queries**: Pull cost data via Steampipe's AWS billing tables.
- 📊 **Compliance Visibility**: Evaluate configurations for security and compliance.
- 📦 **MCP Protocol Support**: Built using [FastMCP](https://modelcontextprotocol.io), ready to plug into AI tools like Claude.

---

## 🛠️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/sunil-kumar-h/steampipe-mcp-server.git
cd steampipe-mcp-server
