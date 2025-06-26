from setuptools import setup, find_packages

setup(
    name="gestify",
    version="0.1.0",  
    author="Vamshi Vishruth J",
    author_email="",
    project_urls={
        "Homepage": "https://github.com/RandomForestPanda/FreeHandsControl",
        "Bug Reports": "https://github.com/RandomForestPanda/FreeHandsControl/issues",
    }
    description="Touchless gesture control for macOS",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/RandomForestPanda/FreeHandsControl",
    packages=find_packages(),
    install_requires=[
        'opencv-python>=4.5.0',
        'mediapipe>=0.8.9',
        'numpy>=1.21.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'gestify-volume=gestify.VolumeHandControl:main',
            'gestify-zoom=gestify.ZoomHandcontrol:main'
        ],
    },
)
