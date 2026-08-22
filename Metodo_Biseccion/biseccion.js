const metodoBiseccion = (a, b, Tol) => {
    const iteracionesCalculadas = calcularIteraciones(a, b, Tol)
    const maxIteraciones = iteracionesCalculadas+1;
    let i = 1, P, FA = Math.log(a) + a, FB = Math.log(b) + b, FP, evaluar, FAFP

    if (FA * FB > 0) {
        console.log("El intervalo dado no garantiza una raíz por el método de bisección.");
        return;
    }

    while (i <= maxIteraciones) {
        P = (a + b) / 2;
        FP = Math.log(P) + P;
        evaluar = (b - a) / 2;

        if (evaluar < Tol) {
            imprimir(i, a, b, P, FA, FP, evaluar, Tol)
            break;
        }
        imprimir(i, a, b, P, FA, FP, evaluar, Tol)
        FAFP = FA * FP;
        if (FAFP > 0) {
            a = P;
            FA = FP;
        } else {
            b = P;
        }
        i++
    }
    console.log(`Num iteraciones Caluladas: +-${iteracionesCalculadas} | Iteraciones ejecutadas: ${i}`)
}

const calcularIteraciones = (a, b, Tol) => {
    let iteraciones = (Math.log10((2 * (b - a)) / Tol)) / Math.log10(2);
    return Math.floor(iteraciones)
}

const imprimir = (i, a, b, P, FA, FP, evaluar, Tol) => {
    console.log(`Iteración: ${i}`);
    console.log(`| i: ${i} | a: ${a} | b: ${b} | P: ${P} | FA: ${FA} | FP: ${FP} | ${evaluar} < ${Tol} = ${evaluar < Tol} |`);
    console.log("\n");
}
metodoBiseccion(0.5, 2, 0.01);

