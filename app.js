const products = [
  { id: "dani-17", name: "Manilla Dani", category: "pulseras", collection: "17 mostacillas", glyph: "✧", description: "Diseño artesanal tejido con 17 mostacillas Miyuki.", photos: ["manilla-dani-1.jpg", "manilla-dani-2.jpg"], variants: [{ label: "Con nudo", price: 60000 }, { label: "Con terminación", price: 65000 }] },
  { id: "tribu-17", name: "Manilla Tribu", category: "pulseras", collection: "17 mostacillas", glyph: "✳", description: "Diseño artesanal tejido con 17 mostacillas Miyuki.", photos: ["manilla-tribu-1.jpg", "manilla-tribu-2.jpg"], variants: [{ label: "Con nudo", price: 60000 }, { label: "Con terminación", price: 65000 }] },
  { id: "piedra-9", name: "Manilla Piedra", category: "pulseras", collection: "9 mostacillas", glyph: "◈", description: "Composición de 9 mostacillas, inspirada en los tonos de la piedra.", variants: [{ label: "Con nudo", price: 35000 }, { label: "Con terminación", price: 40000 }] },
  { id: "arcoiris-9", name: "Manilla Arcoíris", category: "pulseras", collection: "9 mostacillas", glyph: "✺", description: "Diseño colorido tejido con 9 mostacillas Miyuki.", variants: [{ label: "Con nudo", price: 35000 }, { label: "Con terminación", price: 40000 }] },
  { id: "piramide-9", name: "Manilla Pirámide", category: "pulseras", collection: "9 mostacillas", glyph: "△", description: "Diseño geométrico tejido con 9 mostacillas Miyuki.", variants: [{ label: "Con nudo", price: 35000 }, { label: "Con terminación", price: 40000 }] },
  { id: "millos-7", name: "Manilla Millos", category: "pulseras", collection: "7 mostacillas", glyph: "✧", description: "Diseño tejido con 7 mostacillas Miyuki.", variants: [{ label: "Con nudo", price: 30000 }, { label: "Con terminación", price: 35000 }] },
  { id: "delica-7", name: "Manilla Delica", category: "pulseras", collection: "7 mostacillas", glyph: "◇", description: "Delicadas cuentas Miyuki en un tejido de 7 mostacillas.", photos: ["manilla-delica-1.jpg", "manilla-delica-2.jpg", "manilla-delica-3.jpg"], variants: [{ label: "Con nudo", price: 30000 }, { label: "Con terminación", price: 35000 }] },
  { id: "love-7", name: "Manilla Love", category: "pulseras", collection: "7 mostacillas", glyph: "♡", description: "Un diseño hecho a mano para llevar cerca.", variants: [{ label: "Con nudo", price: 30000 }, { label: "Con terminación", price: 35000 }] },
  { id: "tauro-7", name: "Manilla Zodiaco Tauro", category: "pulseras", collection: "7 mostacillas · zodiaco", zodiac: "tauro", glyph: "♉", description: "Pulsera zodiacal inspirada en el signo de Tauro.", variants: [{ label: "Con nudo", price: 30000 }, { label: "Con terminación", price: 35000 }] },
  { id: "escorpio-7", name: "Manilla Zodiaco Escorpio", category: "pulseras", collection: "7 mostacillas · zodiaco", zodiac: "escorpio", glyph: "♏", description: "Pulsera zodiacal inspirada en el signo de Escorpio.", variants: [{ label: "Con nudo", price: 30000 }, { label: "Con terminación", price: 35000 }] },
  { id: "leo-7", name: "Manilla Zodiaco Leo", category: "pulseras", collection: "7 mostacillas · zodiaco", zodiac: "leo", glyph: "♌", description: "Pulsera zodiacal inspirada en el signo de Leo.", variants: [{ label: "Con nudo", price: 30000 }, { label: "Con terminación", price: 35000 }] },
  { id: "geminis-7", name: "Manilla Zodiaco Géminis", category: "pulseras", collection: "7 mostacillas · zodiaco", zodiac: "geminis", glyph: "♊", description: "Pulsera zodiacal inspirada en el signo de Géminis.", variants: [{ label: "Con nudo", price: 30000 }, { label: "Con terminación", price: 35000 }] },
  { id: "capricornio-7", name: "Manilla Zodiaco Capricornio", category: "pulseras", collection: "7 mostacillas · zodiaco", zodiac: "capricornio", glyph: "♑", description: "Pulsera zodiacal inspirada en el signo de Capricornio.", variants: [{ label: "Con nudo", price: 30000 }, { label: "Con terminación", price: 35000 }] },
  { id: "libra-7", name: "Manilla Zodiaco Libra", category: "pulseras", collection: "7 mostacillas · zodiaco", zodiac: "libra", glyph: "♎", description: "Pulsera zodiacal inspirada en el signo de Libra.", variants: [{ label: "Con nudo", price: 30000 }, { label: "Con terminación", price: 35000 }] },
  { id: "manilla-42", name: "Manilla 42", category: "pulseras", collection: "7 mostacillas", glyph: "✦", description: "Diseño tejido a mano con cuentas Miyuki.", variants: [{ label: "Con nudo", price: 30000 }, { label: "Con terminación", price: 35000 }] },
  { id: "glori-5", name: "Manilla Glori", category: "pulseras", collection: "5 mostacillas", glyph: "✿", description: "Diseño artesanal tejido con 5 mostacillas Miyuki.", variants: [{ label: "Con nudo", price: 25000 }, { label: "Con terminación", price: 30000 }] },
  { id: "colombia-5", name: "Manilla Colombia", category: "pulseras", collection: "5 mostacillas", glyph: "✺", description: "Diseño tejido con cuentas Miyuki en colores vivos.", photos: ["manilla-colombia-1.jpg", "manilla-colombia-2.jpg", "manilla-colombia-3.jpg", "manilla-colombia-4.jpg"], variants: [{ label: "Con nudo", price: 25000 }, { label: "Con terminación", price: 30000 }] },
  { id: "delica-5", name: "Manilla Delica", category: "pulseras", collection: "5 mostacillas", glyph: "◇", description: "Cuentas Miyuki Delica en una pieza delicada y ligera.", variants: [{ label: "Con nudo", price: 25000 }, { label: "Con terminación", price: 30000 }] },
  { id: "llavero-pinguino", name: "Pingüino + Corazones", category: "llaveros", collection: "Llavero", glyph: "♡", description: "Un detalle tejido con cuentas Miyuki y corazón.", price: 20000 },
  { id: "llavero-mariposa", name: "Mariposa + Girasoles", category: "llaveros", collection: "Llavero", glyph: "✿", description: "Mariposa y girasoles en un diseño hecho a mano.", price: 20000 },
  { id: "llavero-girasol", name: "Girasol + Insectos", category: "llaveros", collection: "Llavero", glyph: "✺", description: "Un pequeño jardín para llevar contigo.", price: 20000 },
  { id: "llavero-princesa", name: "Princesa Grumosa", category: "llaveros", collection: "Llavero", glyph: "✧", description: "Llavero artesanal decorado con mostacillas Miyuki.", price: 20000 },
  { id: "colgante-dos-gatos", name: "Dos Gatos", category: "colgantes", collection: "Colgante para celular", glyph: "☾", description: "Un par de gatos tejidos para adornar tu celular.", price: 15054 },
  { id: "colgante-gato", name: "Gato Cabeza", category: "colgantes", collection: "Colgante para celular", glyph: "猫", description: "Un pequeño compañero hecho con cuentas Miyuki.", price: 14847 },
  { id: "prendedor-gorro-rojo", name: "Gorro Navidad Rojo y Verde", category: "prendedores", collection: "Prendedor", glyph: "✳", description: "Prendedor festivo elaborado con mostacillas Miyuki.", price: 18504 },
  { id: "prendedor-gorro", name: "Gorro Navideño", category: "prendedores", collection: "Prendedor", glyph: "❋", description: "Un detalle navideño tejido a mano.", price: 14254 },
];

const categoryNames = {
  pulseras: "Pulsera",
  llaveros: "Llavero",
  colgantes: "Colgante",
  prendedores: "Prendedor",
};

const zodiacNames = {
  tauro: "Tauro",
  escorpio: "Escorpio",
  leo: "Leo",
  geminis: "Géminis",
  capricornio: "Capricornio",
  libra: "Libra",
};

const currency = new Intl.NumberFormat("es-CO", {
  style: "currency",
  currency: "COP",
  maximumFractionDigits: 0,
});

const cart = new Map();
let activeCategory = "todos";
let activeZodiac = "";

const productGrid = document.querySelector("#product-grid");
const catalogCount = document.querySelector("#catalog-count");
const searchInput = document.querySelector("#catalog-search");
const orderLines = document.querySelector("#order-lines");

function priceText(value) {
  return currency.format(value);
}

function productCard(product) {
  const choice = product.variants
    ? `<div class="product-choice">
        <label for="variant-${product.id}">Acabado</label>
        <select id="variant-${product.id}" data-variant="${product.id}">
          ${product.variants.map((variant, index) => `<option value="${index}">${variant.label} · ${priceText(variant.price)}</option>`).join("")}
        </select>
      </div>`
    : "";
  const initialPrice = product.variants ? product.variants[0].price : product.price;
  const image = product.photos?.length
    ? `<img class="product-photo" src="assets/productos/${product.photos[0]}" alt="${product.name}, foto 1 de ${product.photos.length}">`
    : `<span class="product-glyph" aria-hidden="true">${product.glyph}</span>`;
  const gallery = product.photos?.length > 1
    ? `<div class="photo-picker" role="group" aria-label="Fotos de ${product.name}">
        ${product.photos.map((_, index) => `<button class="photo-dot${index === 0 ? " is-active" : ""}" type="button" data-photo="${product.id}" data-photo-index="${index}" aria-label="Ver foto ${index + 1} de ${product.name}" aria-pressed="${index === 0}"></button>`).join("")}
      </div>`
    : "";

  return `<article class="product-card">
    <div class="product-art" data-category="${product.category}">
      <span class="product-category">${categoryNames[product.category]}</span>
      ${image}
      ${gallery}
    </div>
    <div class="product-content">
      <p class="product-kicker">${product.collection}</p>
      <h3>${product.name}</h3>
      <p class="product-description">${product.description}</p>
      ${choice}
      <div class="product-bottom">
        <span class="product-price" data-price-for="${product.id}">${priceText(initialPrice)}</span>
        <button class="add-button" type="button" data-add="${product.id}"><span aria-hidden="true">＋</span> Agregar</button>
      </div>
    </div>
  </article>`;
}

function renderCatalog() {
  const query = searchInput.value.trim().toLocaleLowerCase("es");
  const visibleProducts = products.filter((product) => {
    const categoryMatches = activeCategory === "todos" || product.category === activeCategory;
    const zodiacMatches = !activeZodiac || product.zodiac === activeZodiac;
    const searchMatches = `${product.name} ${product.collection} ${product.description}`
      .toLocaleLowerCase("es")
      .includes(query);
    return categoryMatches && zodiacMatches && searchMatches;
  });

  catalogCount.textContent = `${visibleProducts.length} ${visibleProducts.length === 1 ? "diseño disponible" : "diseños disponibles"}`;
  productGrid.innerHTML = visibleProducts.length
    ? visibleProducts.map(productCard).join("")
    : `<p class="empty-results">No encontramos diseños con esos filtros. Prueba otra búsqueda o categoría.</p>`;
}

function cartKey(product, variant) {
  return `${product.id}::${variant ? variant.label : "único"}`;
}

function addProduct(productId) {
  const product = products.find((item) => item.id === productId);
  if (!product) return;

  let variant = null;
  if (product.variants) {
    const selector = document.querySelector(`[data-variant="${product.id}"]`);
    variant = product.variants[Number(selector.value)];
  }

  const key = cartKey(product, variant);
  const current = cart.get(key);
  cart.set(key, {
    product,
    variant,
    price: variant ? variant.price : product.price,
    quantity: current ? current.quantity + 1 : 1,
  });
  renderOrder();
}

function renderOrder() {
  const lines = [...cart.entries()];
  const quantity = lines.reduce((sum, [, line]) => sum + line.quantity, 0);
  const total = lines.reduce((sum, [, line]) => sum + line.quantity * line.price, 0);

  document.querySelector("#bag-count").textContent = String(quantity);
  document.querySelector("#order-quantity").textContent = String(quantity);
  document.querySelector("#order-total").textContent = priceText(total);
  document.querySelector("#copy-order").disabled = quantity === 0;
  document.querySelector("#clear-order").disabled = quantity === 0;

  if (!lines.length) {
    orderLines.innerHTML = `<div class="empty-order"><strong>Tu pedido comienza con una intención.</strong><span>Agrega tus diseños favoritos para ver aquí el resumen.</span></div>`;
    return;
  }

  orderLines.innerHTML = lines.map(([key, line]) => {
    const variantText = line.variant ? ` · ${line.variant.label}` : "";
    return `<div class="order-line">
      <div>
        <span class="order-line-name">${line.product.name}</span>
        <span class="order-line-variant">${line.product.collection}${variantText}</span>
      </div>
      <div class="quantity-control" aria-label="Cantidad de ${line.product.name}">
        <button type="button" data-quantity="-1" data-key="${encodeURIComponent(key)}" aria-label="Restar una unidad">−</button>
        <span>${line.quantity}</span>
        <button type="button" data-quantity="1" data-key="${encodeURIComponent(key)}" aria-label="Agregar una unidad">＋</button>
      </div>
      <span class="order-line-price">${priceText(line.quantity * line.price)}</span>
    </div>`;
  }).join("");
}

function updateQuantity(encodedKey, change) {
  const key = decodeURIComponent(encodedKey);
  const line = cart.get(key);
  if (!line) return;
  line.quantity += change;
  if (line.quantity <= 0) cart.delete(key);
  else cart.set(key, line);
  renderOrder();
}

function orderText() {
  const lines = [...cart.values()];
  const details = lines.map((line) => {
    const variantText = line.variant ? ` (${line.variant.label})` : "";
    return `- ${line.quantity} x ${line.product.name}${variantText}: ${priceText(line.quantity * line.price)}`;
  });
  const total = lines.reduce((sum, line) => sum + line.quantity * line.price, 0);
  return ["Hola, quisiera consultar disponibilidad para este pedido:", ...details, `Total de referencia: ${priceText(total)}`, "Gracias."].join("\n");
}

async function copyOrder() {
  const feedback = document.querySelector("#copy-feedback");
  try {
    await navigator.clipboard.writeText(orderText());
    feedback.textContent = "Resumen copiado. Ya puedes compartirlo con Miyuki Accesorios.";
  } catch (error) {
    const textArea = document.createElement("textarea");
    textArea.value = orderText();
    textArea.setAttribute("readonly", "");
    textArea.style.position = "fixed";
    textArea.style.opacity = "0";
    document.body.append(textArea);
    textArea.select();
    const copied = document.execCommand("copy");
    textArea.remove();
    if (!copied) {
      feedback.textContent = "No se pudo copiar automáticamente. Selecciona y copia el resumen de tu pedido.";
      return;
    }
    feedback.textContent = "Resumen copiado. Ya puedes compartirlo con Miyuki Accesorios.";
  }
}

document.querySelector("#category-filters").addEventListener("click", (event) => {
  const button = event.target.closest("[data-category]");
  if (!button) return;
  activeCategory = button.dataset.category;
  activeZodiac = "";
  document.querySelector("#zodiac-select").value = "";
  document.querySelector("#zodiac-feedback").textContent = "";
  document.querySelectorAll(".filter-button").forEach((filter) => {
    const isActive = filter === button;
    filter.classList.toggle("is-active", isActive);
    filter.setAttribute("aria-pressed", String(isActive));
  });
  renderCatalog();
});

searchInput.addEventListener("input", renderCatalog);

productGrid.addEventListener("change", (event) => {
  const selector = event.target.closest("[data-variant]");
  if (!selector) return;
  const product = products.find((item) => item.id === selector.dataset.variant);
  const selectedVariant = product.variants[Number(selector.value)];
  document.querySelector(`[data-price-for="${product.id}"]`).textContent = priceText(selectedVariant.price);
});

productGrid.addEventListener("click", (event) => {
  const photoButton = event.target.closest("[data-photo]");
  if (photoButton) {
    const product = products.find((item) => item.id === photoButton.dataset.photo);
    const index = Number(photoButton.dataset.photoIndex);
    if (!product?.photos[index]) return;

    const card = photoButton.closest(".product-card");
    const image = card.querySelector(".product-photo");
    image.src = `assets/productos/${product.photos[index]}`;
    image.alt = `${product.name}, foto ${index + 1} de ${product.photos.length}`;
    card.querySelectorAll(".photo-dot").forEach((button) => {
      const isActive = button === photoButton;
      button.classList.toggle("is-active", isActive);
      button.setAttribute("aria-pressed", String(isActive));
    });
    return;
  }

  const button = event.target.closest("[data-add]");
  if (button) addProduct(button.dataset.add);
});

orderLines.addEventListener("click", (event) => {
  const button = event.target.closest("[data-quantity]");
  if (button) updateQuantity(button.dataset.key, Number(button.dataset.quantity));
});

document.querySelector("#clear-order").addEventListener("click", () => {
  cart.clear();
  document.querySelector("#copy-feedback").textContent = "";
  renderOrder();
});

document.querySelector("#copy-order").addEventListener("click", copyOrder);

document.querySelector("#find-zodiac").addEventListener("click", () => {
  const zodiac = document.querySelector("#zodiac-select").value;
  const feedback = document.querySelector("#zodiac-feedback");
  if (!zodiac) {
    feedback.textContent = "Elige un signo para encontrar tu diseño.";
    return;
  }
  activeCategory = "pulseras";
  activeZodiac = zodiac;
  searchInput.value = "";
  document.querySelectorAll(".filter-button").forEach((filter) => {
    const isActive = filter.dataset.category === "pulseras";
    filter.classList.toggle("is-active", isActive);
    filter.setAttribute("aria-pressed", String(isActive));
  });
  feedback.textContent = `Encontramos la pulsera de ${zodiacNames[zodiac]}.`;
  renderCatalog();
  document.querySelector("#catalogo").scrollIntoView({ behavior: "smooth" });
});

renderCatalog();
renderOrder();
