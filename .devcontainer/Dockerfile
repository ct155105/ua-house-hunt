FROM python:3

RUN pip install -e 'git+https://github.com/ct155105/ct_python_helpers.git@main#egg=ds_helpers&subdirectory=data_science_helpers/pkg'
RUN pip install -e 'git+https://github.com/ct155105/ct_python_helpers.git@main#egg=df_helpers&subdirectory=dataframe_wrappers/pkg'
RUN pip install -e 'git+https://github.com/ct155105/ct_python_helpers.git@main#egg=ct_math&subdirectory=math_helpers/pkg'

# # [Optional] Allow the vscode user to pip install globally w/o sudo
# ENV PIP_TARGET=/usr/local/pip-global
# ENV PYTHONPATH=${PIP_TARGET}:${PYTHONPATH}
# ENV PATH=${PIP_TARGET}/bin:${PATH}
# RUN if ! cat /etc/group | grep -e "^pip-global:" > /dev/null 2>&1; then groupadd -r pip-global; fi \
#     && usermod -a -G pip-global vscode \
#     && umask 0002 && mkdir -p ${PIP_TARGET} \
#     && chown :pip-global ${PIP_TARGET} \
#     && ( [ ! -f "/etc/profile.d/00-restore-env.sh" ] || sed -i -e "s/export PATH=/export PATH=\/usr\/local\/pip-global:/" /etc/profile.d/00-restore-env.sh )

# # [Option] Install Node.js
# ARG INSTALL_NODE="true"
# ARG NODE_VERSION="lts/*"
# RUN if [ "${INSTALL_NODE}" = "true" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi