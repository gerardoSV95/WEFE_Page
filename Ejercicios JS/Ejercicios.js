
const nPrimo=(numero=undefined)=>{
    if (numero===undefined) return console.warn("No se ingreso un numero.");
    if (numero!== "number") return console.error(`El valor "${numero}" ingresado, no es un numero.`);
    if (Math.sign[numero]===-1)return console.error("El numero no puede ser negativo");

    if(numero%3===1) return console.log(`${numero} es un numero primo.`);
    else return console.log(`El numero "${numero} no es un numero primo.`);
}