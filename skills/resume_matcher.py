#!/usr/bin/env python3
"""Resume Matcher - Matches resumes against job descriptions."""

import sys
import fitz  # PyMuPDF


def extract_text_from_pdf(pdf_path):
    """Extract text content from a PDF file."""
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None


def extract_skills(text):
    """Extract skills from text content."""
    skills = set()
    skill_keywords = [
        "python", "r", "machine learning", "data visualization", "sql",
        "statistical analysis", "pandas", "numpy", "scikit-learn",
        "javascript", "java", "c++", "typescript", "react", "angular",
        "vue", "node.js", "django", "flask", "fastapi", "tensorflow",
        "pytorch", "keras", "docker", "kubernetes", "aws", "azure",
        "gcp", "git", "linux", "bash", "mongodb", "postgresql", "mysql"
    ]
    
    text_lower = text.lower()
    for skill in skill_keywords:
        if skill in text_lower:
            skills.add(skill)
    
    return skills


def parse_job_description(jd_path):
    """Parse job description file and extract required skills."""
    try:
        with open(jd_path, 'r') as f:
            content = f.read()
        
        # Extract skills section
        skills = set()
        lines = content.split('\n')
        in_skills_section = False
        
        for line in lines:
            if "Required Skills" in line or "Skills" in line:
                in_skills_section = True
                continue
            
            if in_skills_section:
                if line.strip().startswith('-'):
                    skill = line.strip()[1:].strip()
                    skills.add(skill.lower())
                elif line.strip() and not line.strip().startswith('-'):
                    # End of skills section
                    break
        
        return content, skills
    except Exception as e:
        print(f"Error reading job description: {e}")
        return None, None


def calculate_match_score(resume_skills, required_skills):
    """Calculate match score between resume and job requirements."""
    if not required_skills:
        return 0
    
    matched = len(resume_skills.intersection(required_skills))
    total = len(required_skills)
    
    return (matched / total) * 100


def print_results(resume_text, jd_content, resume_skills, required_skills, match_score):
    """Print detailed matching results."""
    print("\n" + "=" * 60)
    print("RESUME MATCHING RESULTS")
    print("=" * 60)
    
    print(f"\nMatch Score: {match_score:.1f}%")
    
    print(f"\n--- Resume Skills Found ({len(resume_skills)}) ---")
    for skill in sorted(resume_skills):
        print(f"  - {skill}")
    
    print(f"\n--- Required Skills ({len(required_skills)}) ---")
    for skill in sorted(required_skills):
        status = "✓" if skill in resume_skills else "✗"
        print(f"  {status} {skill}")
    
    matched_count = len(resume_skills.intersection(required_skills))
    print(f"\n--- Summary ---")
    print(f"Matched Skills: {matched_count}/{len(required_skills)}")
    print(f"Missing Skills: {len(required_skills) - matched_count}")


def main():
    """Main entry point for the resume matcher."""
    if len(sys.argv) != 3:
        print("Usage: python skills/resume_matcher.py <path_to_resume.pdf> <job_description.txt>")
        sys.exit(1)
    
    resume_path = sys.argv[1]
    jd_path = sys.argv[2]
    
    # Extract text from PDF resume
    resume_text = extract_text_from_pdf(resume_path)
    if not resume_text:
        print("Failed to read resume PDF")
        sys.exit(1)
    
    # Parse job description
    jd_content, required_skills = parse_job_description(jd_path)
    if not jd_content or not required_skills:
        print("Failed to parse job description")
        sys.exit(1)
    
    # Extract skills from resume
    resume_skills = extract_skills(resume_text)
    
    # Calculate match score
    match_score = calculate_match_score(resume_skills, required_skills)
    
    # Print results
    print_results(resume_text, jd_content, resume_skills, required_skills, match_score)


if __name__ == '__main__':
    main()
