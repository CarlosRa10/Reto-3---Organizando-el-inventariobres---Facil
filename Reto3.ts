export{}
interface Toy {
  name: string;
  quantity: number;
  category: string;
}

type Inventory = Toy[];

// Define el tipo del objeto acumulador (acc)
type OrganizedInventory = {
  [category: string]: {
    [name: string]: number;
  };
};

function organizeInventory(inventory: Inventory): OrganizedInventory {
  return inventory.reduce((acc, curr) => {
    acc[curr.category] ??= {}; // Inicializa la categoría si es null o undefined -?? Nullish-
    acc[curr.category][curr.name] = (acc[curr.category][curr.name] ?? 0) + curr.quantity; // Suma la cantidad
    return acc;
  }, {} as OrganizedInventory); // Asegura que el acumulador es del tipo OrganizedInventory
}

// Ejemplo de uso:
const inventory: Inventory = [
  { name: 'doll', quantity: 5, category: 'toys' },
  { name: 'car', quantity: 3, category: 'toys' },
  { name: 'ball', quantity: 2, category: 'sports' },
  { name: 'car', quantity: 2, category: 'toys' },
  { name: 'racket', quantity: 4, category: 'sports' }
];

console.log(organizeInventory(inventory));

const inventory2: Inventory = [
  { name: 'book', quantity: 10, category: 'education' },
  { name: 'book', quantity: 5, category: 'education' },
  { name: 'paint', quantity: 3, category: 'art' }
];

console.log(organizeInventory(inventory2));