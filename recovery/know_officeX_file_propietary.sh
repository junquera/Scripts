for i in *; do 
    echo "El propietario de $i es "$(unzip -c $i docProps/core.xml | grep -oPm1 "(?<=<dc:creator>)[^<]+"); 
done;
