# Assignment 1: AI Text Transformer

## Overview

This assignment demonstrates the creation of an AI-powered text transformation pipeline using LangChain and Ollama. The system analyzes input text and provides structured output including a summary, tone analysis, and an improved version of the text.

## Features

- **Text Analysis**: Analyzes paragraphs for key points and tone
- **Structured Output**: Provides consistent formatting with SUMMARY, TONE, and IMPROVED VERSION sections
- **LangChain Integration**: Uses PromptTemplate and StrOutputParser for robust text processing
- **Ollama LLM**: Leverages local Mistral model for text generation

## Requirements

- Python 3.8+
- Ollama installed and running
- Mistral model pulled (`ollama pull mistral`)
- Required packages: langchain-core, langchain-ollama

## Installation

1. Ensure Ollama is installed and running:
   ```bash
   ollama serve
   ```

2. Pull the Mistral model:
   ```bash
   ollama pull mistral
   ```

3. Install required Python packages:
   ```bash
   pip install langchain-core langchain-ollama
   ```

## Usage

Run the assignment:

```bash
python assignment1_text_transformer.py
```

The program will:
1. Create a text transformation chain
2. Process a sample paragraph
3. Display the raw LLM output
4. Parse and display structured results

## Code Structure

### `create_text_transformer()`
- Initializes Ollama LLM with Mistral model
- Creates a detailed prompt template for text analysis
- Sets up output parsing with StrOutputParser
- Returns a LangChain chain (prompt → LLM → parser)

### `parse_transformer_output(output_string)`
- Parses raw string output into structured dictionary
- Extracts SUMMARY, TONE, and IMPROVED VERSION sections
- Returns organized results for easy access

### `main()`
- Demonstrates the complete pipeline
- Shows input processing and output formatting
- Handles errors gracefully

## Expected Output Format

The system produces output in this exact format:

```
SUMMARY:
[3-4 line summary of main points]

TONE:
[Formal / Casual / Technical]

IMPROVED VERSION:
[Enhanced paragraph with better flow and clarity]
```

## Learning Objectives

- Understanding LangChain chains and pipelines
- Working with PromptTemplate for structured prompts
- Using StrOutputParser for text output handling
- Integrating Ollama models with LangChain
- Parsing LLM outputs into structured data

## Example

Input paragraph about the "quick brown fox" pangram produces:
- A concise summary of its purpose
- Tone identification (likely "Casual" or "Informative")
- An improved version with better vocabulary and flow</content>
<parameter name="filePath">c:\Users\jhanv\OneDrive\Documents\ollama\README_assignment1.md