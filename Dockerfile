FROM continuumio/miniconda

RUN useradd -ms /bin/bash sites
COPY --chown=sites:sites . /usr/local/sites
COPY requirements.txt requirements.txt

RUN conda update -n base -c defaults conda && \
    conda create -n sites python=3.7 && \
    conda install -n sites -c rdkit rdkit -y && \
    conda install -n sites pip -y && \
    echo "source activate sites" >> /home/sites/.bashrc

RUN bash -c "source activate sites && pip install -r requirements.txt && rm requirements.txt"

USER sites
CMD source /home/sites/.bashrc
WORKDIR /usr/local/sites
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/conda/lib/
ENV PYTHONPATH=${PYTHONPATH}:/opt/conda/envs/sites/bin:/usr/local/sites
