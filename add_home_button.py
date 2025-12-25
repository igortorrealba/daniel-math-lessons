#!/usr/bin/env python3
"""
Script to add HOME button to all lesson, app, and worksheet HTML files.
"""
import os
import re
from pathlib import Path

# Define the education directory
BASE_DIR = Path(__file__).parent

# HOME button CSS and HTML to be added
HOME_BUTTON_CSS = """.home-button {
    position: fixed;
    top: 20px;
    right: 20px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 12px 24px;
    border-radius: 25px;
    text-decoration: none;
    font-weight: bold;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    z-index: 1000;
    transition: transform 0.2s, box-shadow 0.2s;
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 16px;
}

.home-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.3);
}

@media print {
    .home-button {
        display: none;
    }
}"""

HOME_BUTTON_HTML = '<a href="../index.html" class="home-button">🏠 Inicio</a>'

def add_home_button(file_path):
    """Add HOME button to a single HTML file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if HOME button already exists
        if 'home-button' in content:
            print(f"  ⏭️  Skipped (already has HOME button): {file_path.name}")
            return False

        # Add CSS before </style>
        if '</style>' in content:
            content = content.replace('</style>', f'{HOME_BUTTON_CSS}</style>')
        else:
            # If no </style> tag, try to add before </head>
            if '</head>' in content:
                style_block = f'<style>{HOME_BUTTON_CSS}</style>'
                content = content.replace('</head>', f'{style_block}</head>')

        # Add HTML button after <body>
        if '<body>' in content:
            content = content.replace('<body>', f'<body>{HOME_BUTTON_HTML}')

        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  ✅ Added HOME button: {file_path.name}")
        return True

    except Exception as e:
        print(f"  ❌ Error processing {file_path.name}: {e}")
        return False

def main():
    """Main function to process all files."""
    print("🚀 Starting to add HOME buttons to all HTML files...")
    print()

    # Find all lesson directories
    lesson_dirs = sorted([d for d in BASE_DIR.iterdir()
                         if d.is_dir() and d.name.startswith('2025')])

    total_files = 0
    processed_files = 0

    for lesson_dir in lesson_dirs:
        print(f"📁 Processing: {lesson_dir.name}")

        # Process Lesson, App, and Worksheet files
        for file_type in ['Lesson_', 'App_', 'Worksheet_']:
            html_files = list(lesson_dir.glob(f'{file_type}*.html'))

            for html_file in html_files:
                total_files += 1
                if add_home_button(html_file):
                    processed_files += 1

        print()

    print("=" * 60)
    print(f"✨ COMPLETE!")
    print(f"   Total files found: {total_files}")
    print(f"   Files updated: {processed_files}")
    print(f"   Files skipped: {total_files - processed_files}")
    print("=" * 60)

if __name__ == '__main__':
    main()
