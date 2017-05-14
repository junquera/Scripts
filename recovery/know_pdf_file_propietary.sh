for i in "*.pdf"; do 
    echo "El propietario de $i es "$(pdfinfo "$i" | grep -oPm1 "Author:"); 
done;
