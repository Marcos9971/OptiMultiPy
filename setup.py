from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()



    setup(
    name='OptiMultiPy',
    version="0.0.1",
    packages=find_packages(),
    install_requires=['matplotlib', 'numpy', 'control'],
    author="Marcos Antônio Leandro",
    author_email="marcos352354@gmail.com",
    keywords='PID' 'otimização' 'ganhos' 'sintonia',
    description="Sintonia do controlador PID utilizando algoritmo de otimização",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    #url="https://github.com/seuusuario/minhabiblioteca",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)