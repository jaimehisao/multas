docker build -f Dockerfile.candidates_mty . -t registry.internal.hisao.org/prod/multas-mty-candidates
docker build -f Dockerfile.candidates_spgg . -t registry.internal.hisao.org/prod/multas-spgg-candidates
docker build -f Dockerfile.updater_mty . -t registry.internal.hisao.org/prod/multas-mty-updater
docker build -f Dockerfile.updater_spgg . -t registry.internal.hisao.org/prod/multas-spgg-updater
docker build -f Dockerfile.candidates . -t registry.internal.hisao.org/prod/candidate-plates
docker build -f Dockerfile.datacleaning . -t registry.internal.hisao.org/prod/plate-data-cleaning

docker push registry.internal.hisao.org/prod/multas-mty-candidates
docker push registry.internal.hisao.org/prod/multas-spgg-candidates
docker push registry.internal.hisao.org/prod/multas-mty-updater
docker push registry.internal.hisao.org/prod/multas-spgg-updater
docker push registry.internal.hisao.org/prod/candidate-plates
docker push registry.internal.hisao.org/prod/plate-data-cleaning

echo ""
echo ""
echo "Built and Pushed 6 Docker Images Successfully"