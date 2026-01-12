# Configuration file for the Sphinx documentation builder.

project = 'Jani Huuhtanen'
copyright = '2024, Jani Huuhtanen'
author = 'Jani Huuhtanen'

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Furo theme
html_theme = 'furo'
html_title = "Jani Huuhtanen"
html_static_path = ['_static']

# Custom CSS
html_css_files = ['custom.css']

# Theme options
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#5C4033",
        "color-brand-content": "#5C4033",
        "color-background-primary": "#f5e9dc",
        "color-background-secondary": "#ece0d1",
        "color-foreground-primary": "#2d2d2d",
        "color-foreground-secondary": "#4a4a4a",
    },
    "dark_css_variables": {
        "color-brand-primary": "#d4a574",
        "color-brand-content": "#d4a574",
    },
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
    "top_of_page_buttons": [],
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/janihuuh",
            "html": """<svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>""",
            "class": "",
        },
        {
            "name": "Google Scholar",
            "url": "https://scholar.google.com/citations?user=T7UqQkEAAAAJ",
            "html": """<svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24"><path d="M12 24a7 7 0 1 1 0-14 7 7 0 0 1 0 14zm0-24L0 9.5l4.838 3.94A8 8 0 0 1 12 9a8 8 0 0 1 7.162 4.44L24 9.5z"/></svg>""",
            "class": "",
        },
        {
            "name": "ORCID",
            "url": "https://orcid.org/0000-0003-2750-4033",
            "html": """<svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24"><path d="M12 0C5.372 0 0 5.372 0 12s5.372 12 12 12 12-5.372 12-12S18.628 0 12 0zM7.369 4.378c.525 0 .947.431.947.947s-.422.947-.947.947a.95.95 0 0 1-.947-.947c0-.525.422-.947.947-.947zm-.722 3.038h1.444v10.041H6.647V7.416zm3.562 0h3.9c3.712 0 5.344 2.653 5.344 5.025 0 2.578-2.016 5.025-5.325 5.025h-3.919V7.416zm1.444 1.303v7.444h2.297c3.272 0 4.022-2.484 4.022-3.722 0-2.016-1.284-3.722-4.097-3.722h-2.222z"/></svg>""",
            "class": "",
        },
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/in/jani-huuhtanen/",
            "html": """<svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>""",
            "class": "",
        },
    ],
}

# Sidebar with navigation
html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/scroll-start.html",
        "sidebar/navigation.html",
        "sidebar/scroll-end.html",
    ],
}
