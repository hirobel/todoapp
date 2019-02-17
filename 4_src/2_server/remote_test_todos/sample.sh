targetid=`cat result/create-testValidateInput1.json | tr -d ' "[]{}' | awk -F: '{ print $5 }' | cut -d "," -f 1`
echo $targetid
