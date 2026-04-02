#!/usr/bin/env python3
"""
BioSkills Scanner - Extracts bioinformatics skills from text using regex.
"""

import re


def scan_bio_skills(text):
    """
    Scan text for bioinformatics-related skills.
    
    Args:
        text (str): The text to scan (e.g., a job description)
    
    Returns:
        dict: Dictionary with categories and found skills
    """
    results = {
        'programming_languages': [],
        'sequencing_tools': [],
        'workflow_managers': []
    }
    
    # Programming languages patterns
    lang_patterns = [
        r'\bPython\b',
        r'\bR\b',
        r'\bPerl\b'
    ]
    
    # Sequencing tools patterns
    tool_patterns = [
        r'\bBWA\b',
        r'\bGATK\b',
        r'\bSamtools\b',
        r'\bBowtie2\b'
    ]
    
    # Workflow managers patterns
    workflow_patterns = [
        r'\bNextflow\b',
        r'\bSnakemake\b'
    ]
    
    # Search for programming languages
    for pattern in lang_patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            if match not in results['programming_languages']:
                results['programming_languages'].append(match)
    
    # Search for sequencing tools
    for pattern in tool_patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            if match not in results['sequencing_tools']:
                results['sequencing_tools'].append(match)
    
    # Search for workflow managers
    for pattern in workflow_patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            if match not in results['workflow_managers']:
                results['workflow_managers'].append(match)
    
    return results


def print_results(results):
    """Print the scan results in a formatted way."""
    print("=" * 50)
    print("BioSkills Scan Results")
    print("=" * 50)
    
    if results['programming_languages']:
        print("\nProgramming Languages:")
        for lang in results['programming_languages']:
            print(f"  - {lang}")
    
    if results['sequencing_tools']:
        print("\nSequencing Tools:")
        for tool in results['sequencing_tools']:
            print(f"  - {tool}")
    
    if results['workflow_managers']:
        print("\nWorkflow Managers:")
        for wf in results['workflow_managers']:
            print(f"  - {wf}")
    
    if not any(results.values()):
        print("\nNo bioinformatics skills found.")
    
    print("=" * 50)


if __name__ == '__main__':
    # Test case with sample job description
    sample_job_description = """
    Bioinformatics Scientist Position
    
    We are seeking a skilled bioinformatician to join our genomics team.
    The ideal candidate should have experience with:
    
    - Programming in Python and R for data analysis
    - Perl scripting for legacy pipeline maintenance
    - Sequencing tools including BWA, GATK, Samtools, and Bowtie2
    - Workflow management using Nextflow or Snakemake
    
    Responsibilities include developing analysis pipelines,
    processing NGS data, and collaborating with wet lab scientists.
    
    Requirements:
    - Strong programming skills in Python
    - Experience with BWA for read alignment
    - Knowledge of GATK best practices
    - Familiarity with Snakemake workflow manager
    
    This role requires expertise in bioinformatics tools and
    the ability to work with large-scale sequencing data.
    """
    
    print("Scanning job description...\n")
    results = scan_bio_skills(sample_job_description)
    print_results(results)
