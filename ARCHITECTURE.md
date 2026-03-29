# Architecture Document

## System Overview
Multi-agent AI system that processes financial data and generates actionable insights.

## Agents
1. Data Agent — Fetch stock data
2. Signal Agent — Detect patterns
3. Decision Agent — Combine insights
4. Explanation Agent — Convert to simple text
5. Action Agent — Display alerts

## Flow
User → Data Agent → Signal Agent → Decision Agent → Explanation → UI

## Error Handling
- Missing data → fallback
- Noise filtering → confidence score
