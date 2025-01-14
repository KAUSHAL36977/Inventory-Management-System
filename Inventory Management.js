// JavaScript code for enhancing interactivity in the Inventory Management System

// Example products array for dynamic rendering
const products = [
  {
    name: "Product 1",
    category: "Electronics",
    price: 299.99,
    stock: 50,
    supplier: "Supplier A",
    image: "https://placehold.co/600x400"
  },
  {
    name: "Product 2",
    category: "Furniture",
    price: 199.99,
    stock: 20,
    supplier: "Supplier B",
    image: "https://placehold.co/600x400"
  },
  {
    name: "Product 3",
    category: "Clothing",
    price: 49.99,
    stock: 100,
    supplier: "Supplier C",
    image: "https://placehold.co/600x400"
  }
];

// Function to render product cards dynamically
function renderProducts() {
  const productsContainer = document.querySelector(".grid");
  productsContainer.innerHTML = ""; // Clear existing content

  products.forEach((product) => {
    const productCard = document.createElement("article");
    productCard.className = "bg-white p-4 rounded shadow";
    productCard.innerHTML = `
      <img
        src="${product.image}"
        alt="Image of ${product.name}"
        class="w-full h-48 object-cover rounded mb-4"
      />
      <h3 class="text-lg font-bold mb-2">${product.name}</h3>
      <p class="text-gray-700">Category: ${product.category}</p>
      <p class="text-gray-700">Price: $${product.price.toFixed(2)}</p>
      <p class="text-gray-700">Stock: ${product.stock}</p>
      <p class="text-gray-700">Supplier: ${product.supplier}</p>
    `;
    productsContainer.appendChild(productCard);
  });
}

// Event listeners for buttons
function setupEventListeners() {
  document.querySelector("a[href='#']").addEventListener("click", (e) => {
    e.preventDefault();
    alert("Feature not implemented yet!");
  });

  const addProductButton = document.querySelector(".bg-green-500");
  if (addProductButton) {
    addProductButton.addEventListener("click", () => {
      const newProduct = {
        name: "New Product",
        category: "Miscellaneous",
        price: 99.99,
        stock: 10,
        supplier: "New Supplier",
        image: "https://placehold.co/600x400"
      };
      products.push(newProduct);
      renderProducts();
      alert("Product added successfully!");
    });
  }

  const removeProductButton = document.querySelector(".bg-red-500");
  if (removeProductButton) {
    removeProductButton.addEventListener("click", () => {
      if (products.length > 0) {
        products.pop();
        renderProducts();
        alert("Last product removed successfully!");
      } else {
        alert("No products to remove!");
      }
    });
  }
}

// Initialize the application
function init() {
  renderProducts();
  setupEventListeners();
}

// Wait for the DOM to load before initializing
document.addEventListener("DOMContentLoaded", init);
