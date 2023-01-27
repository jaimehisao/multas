docker build -f Dockerfile.mty . -t registry.internal.hisao.org/prod/multas-mty
docker build -f Dockerfile.spgg . -t registry.internal.hisao.org/prod/multas-spgg
docker build -f Dockerfile.candidates . -t registry.internal.hisao.org/prod/candidate-plates
docker build -f Dockerfile.datacleaning . -t registry.internal.hisao.org/prod/plate-data-cleaning

docker push registry.internal.hisao.org/prod/multas-mty
docker push registry.internal.hisao.org/prod/multas-spgg
docker push registry.internal.hisao.org/prod/candidate-plates
docker push registry.internal.hisao.org/prod/plate-data-cleaning

echo ""
echo ""
echo "Built and Pushed 4 Docker Images Successfully"