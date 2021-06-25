#!/bin/bash
################################
## Many thanks to DeepSociety ##
################################
git clone https://github.com/DeepSociety/best-ngrok 2>&1
mv best-ngrok/ngrok $PWD
rm -rf best-ngrok
echo -e "Reinicie o script"