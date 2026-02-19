

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM


def create_text_transformer():
    """
    Creates a text transformation pipeline with prompt template and string output parser.
    Returns a chain that can process text transformations.
    """
    
    # Initialize the Ollama LLM
    llm = OllamaLLM(model="mistral")
    
    # Create a detailed prompt template for text transformation
    prompt_template = PromptTemplate(
        input_variables=["paragraph"],
        template="""Analyze and transform the following paragraph. Provide your response in this exact format:

SUMMARY:
[Provide a 3-4 line summary of the main points]

TONE:
[Identify if the tone is Formal / Casual / Technical]

IMPROVED VERSION:
[Provide an improved version of the paragraph with better flow, vocabulary, and clarity]

Paragraph to analyze:
{paragraph}

Please provide the response in the format specified above."""
    )
    
    # Create the output parser
    output_parser = StrOutputParser()
    
    # Chain components together: prompt -> model -> parser
    chain = prompt_template | llm | output_parser
    
    return chain


def parse_transformer_output(output_string: str) -> dict:
    """
    Parses the string output from the transformer into structured format.
    
    Args:
        output_string: Raw string output from the LLM chain
        
    Returns:
        Dictionary containing summary, tone, and improved_version
    """
    sections = {
        'summary': '',
        'tone': '',
        'improved_version': ''
    }
    
    # Split output into sections
    current_section = None
    current_content = []
    
    for line in output_string.split('\n'):
        line = line.strip()
        
        if line.startswith('SUMMARY:'):
            if current_section and current_content:
                sections[current_section] = '\n'.join(current_content).strip()
            current_section = 'summary'
            current_content = []
        elif line.startswith('TONE:'):
            if current_section and current_content:
                sections[current_section] = '\n'.join(current_content).strip()
            current_section = 'tone'
            current_content = []
        elif line.startswith('IMPROVED VERSION:'):
            if current_section and current_content:
                sections[current_section] = '\n'.join(current_content).strip()
            current_section = 'improved_version'
            current_content = []
        elif line and current_section:
            current_content.append(line)
    
    # Don't forget the last section
    if current_section and current_content:
        sections[current_section] = '\n'.join(current_content).strip()
    
    return sections


def main():
    """
    Main function demonstrating the text transformer pipeline.
    """
    print("=" * 70)
    print("Assignment 1: AI Text Transformer using StrOutputParser")
    print("=" * 70)
    
    # Create the transformer chain
    chain = create_text_transformer()
    
    # Example paragraph
    paragraph = """
    The quick brown fox jumps over the lazy dog. This is a well-known pangram that contains 
    every letter of the English alphabet. It is often used for testing fonts and keyboards. 
    The sentence has been around for many years and is still widely used today in various 
    applications and educational settings.
    """
    
    print("\nInput Paragraph:")
    print("-" * 70)
    print(paragraph.strip())
    print("-" * 70)
    
    try:
        # Run the chain
        print("\nProcessing with LLM (using StrOutputParser)...")
        result = chain.invoke({"paragraph": paragraph})
        
        print("\nRaw Output from Chain:")
        print("-" * 70)
        print(result)
        print("-" * 70)
        
        # Parse the output into structured format
        parsed = parse_transformer_output(result)
        
        print("\nStructured Results:")
        print("-" * 70)
        print(f"\n SUMMARY:\n{parsed['summary']}\n")
        print(f" DETECTED TONE:\n{parsed['tone']}\n")
        print(f" IMPROVED VERSION:\n{parsed['improved_version']}")
        print("-" * 70)
        
    except Exception as e:
        print(f"\nError during processing: {e}")
        raise


if __name__ == "__main__":
    main()
