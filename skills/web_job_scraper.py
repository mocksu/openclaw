#!/usr/bin/env python3
"""
Web Job Scraper - Scrapes job descriptions from web pages using Playwright.
Extracts bioinformatics skills using the bio_skills_scanner module.
"""

import sys
from playwright.sync_api import sync_playwright
from skills.bio_skills_scanner import scan_bio_skills, print_results


def extract_job_description_text(page):
    """
    Extract job description text from a LinkedIn-style job page.
    
    Args:
        page: Playwright page object
    
    Returns:
        str: Extracted job description text
    """
    # Try to find common job description elements on LinkedIn
    selectors = [
        'div.job-description-text',
        'div.jobs-job-details__description',
        '[data-automation="job-description"]',
        '.jobs-description-content',
        'p'
    ]
    
    text_parts = []
    
    for selector in selectors:
        elements = page.query_selector_all(selector)
        if elements:
            for element in elements:
                text = element.inner_text()
                if text.strip():
                    text_parts.append(text)
    
    # If no specific selectors found, try to get all visible text
    if not text_parts:
        body = page.query_selector('body')
        if body:
            text_parts.append(body.inner_text())
    
    return '\n'.join(text_parts)


def scrape_job_description(url):
    """
    Scrape job description from a URL using Playwright.
    
    Args:
        url (str): The URL to scrape
    
    Returns:
        str: Extracted job description text
    """
    with sync_playwright() as p:
        # Launch browser in headless mode for testing
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            print(f"Loading URL: {url}")
            page.goto(url, wait_until='networkidle', timeout=30000)
            
            # Wait for job description to load
            page.wait_for_timeout(2000)
            
            # Extract the text
            job_text = extract_job_description_text(page)
            
        except Exception as e:
            print(f"Error scraping page: {e}")
            job_text = ""
        
        finally:
            browser.close()
    
    return job_text


def main():
    """Main function to scrape and analyze a job description."""
    # Dummy LinkedIn job URL for testing
    test_url = "https://www.linkedin.com/jobs/view/1234567890"
    
    print("Web Job Scraper - Bioinformatics Skills Extraction")
    print("=" * 50)
    print(f"\nTarget URL: {test_url}")
    print("\nNote: This is a dummy URL for testing purposes.")
    print("Replace with actual LinkedIn job URL to scrape real data.\n")
    
    # Scrape the job description
    job_description = scrape_job_description(test_url)
    
    if not job_description.strip():
        print("No job description text found. Using fallback test data.")
        
        # Fallback test data for demonstration
        job_description = """
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
    
    # Scan for bioinformatics skills
    print("\nScanning job description for bioinformatics skills...\n")
    results = scan_bio_skills(job_description)
    
    # Print the results
    print_results(results)


if __name__ == '__main__':
    main()
