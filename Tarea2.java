class Nodo {
    int dato;
    Nodo noda, nodb, nodc; //a, b y c son referencias individuales
    Nodo(int dato) {
        this.dato = dato; //dato nodo -> numero
    }
}
public class Tarea2 {

    static void buscar(Nodo n, int x) {
        if (n == null) return;

        if (n.dato == x) {
            System.out.println("Nodo: " + n.dato);
            return;
        }
        buscar(n.noda, x);
        buscar(n.nodb, x);
        buscar(n.nodc, x);
    }
    public static void main(String[] args) {
        Nodo head = new Nodo(20);
        Nodo n23 = new Nodo(23);
        Nodo n19 = new Nodo(19);
        Nodo n57 = new Nodo(57);
        Nodo n67 = new Nodo(67);
        Nodo n99 = new Nodo(99);

        head.noda = n23;
        head.nodb = n19;
        n23.nodb = n57;
        n19.nodc = n67;
        n67.nodb = n99;
        //no pongo los null pq java ya los define
        buscar(head, 99);
        buscar(head, 57);
    }
}