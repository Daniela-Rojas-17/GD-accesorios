from __future__ import annotations

import base64
from copy import deepcopy
from datetime import date, timedelta
from math import ceil
from pathlib import Path
import re

import streamlit as st


ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"
IVA_RATE = 0.19
HOURS_PER_DAY = 4
RESTOCK_DAYS = 3
STYLE_OPTIONS = ("minimalista", "colorido", "elegante")
OCCASION_OPTIONS = ("diario", "fiesta", "regalo")
INITIAL_INVENTORY = {
    "delica": {"name": "Cuentas Miyuki Delica 11/0", "unit": "g", "stock": 120, "cost": 900},
    "rocalla": {"name": "Rocalla Miyuki 8/0", "unit": "g", "stock": 80, "cost": 700},
    "hilo": {"name": "Hilo Nymo", "unit": "m", "stock": 200, "cost": 150},
    "cierre": {"name": "Cierre metálico", "unit": "unidad", "stock": 30, "cost": 1500},
    "gancho": {"name": "Gancho para aretes", "unit": "par", "stock": 25, "cost": 1200},
    "dije": {"name": "Dije decorativo", "unit": "unidad", "stock": 15, "cost": 2500},
    "cristal": {"name": "Cristal facetado", "unit": "unidad", "stock": 60, "cost": 400},
}
CATEGORIES = {
    "Todos": "todos",
    "Pulseras": "pulseras",
    "Llaveros": "llaveros",
    "Colgantes": "colgantes",
    "Prendedores": "prendedores",
}
ZODIAC_SIGNS = {
    "Tauro": ("tauro", "♉"),
    "Escorpio": ("escorpio", "♏"),
    "Leo": ("leo", "♌"),
    "Géminis": ("geminis", "♊"),
    "Capricornio": ("capricornio", "♑"),
    "Libra": ("libra", "♎"),
}
PRODUCTS = [
    {"id": "dani-17", "name": "Manilla Dani", "category": "pulseras", "collection": "17 mostacillas", "symbol": "✧", "description": "Diseño artesanal tejido con 17 mostacillas Miyuki.", "photos": ["manilla-dani-1.jpg", "manilla-dani-2.jpg"], "variants": [("Con nudo", 60000), ("Con terminación", 65000)]},
    {"id": "tribu-17", "name": "Manilla Tribu", "category": "pulseras", "collection": "17 mostacillas", "symbol": "✳", "description": "Diseño artesanal tejido con 17 mostacillas Miyuki.", "photos": ["manilla-tribu-1.jpg", "manilla-tribu-2.jpg"], "variants": [("Con nudo", 60000), ("Con terminación", 65000)]},
    {"id": "piedra-9", "name": "Manilla Piedra", "category": "pulseras", "collection": "9 mostacillas", "symbol": "◈", "description": "Composición de 9 mostacillas, inspirada en los tonos de la piedra.", "variants": [("Con nudo", 35000), ("Con terminación", 40000)]},
    {"id": "arcoiris-9", "name": "Manilla Arcoíris", "category": "pulseras", "collection": "9 mostacillas", "symbol": "✺", "description": "Diseño colorido tejido con 9 mostacillas Miyuki.", "variants": [("Con nudo", 35000), ("Con terminación", 40000)]},
    {"id": "piramide-9", "name": "Manilla Pirámide", "category": "pulseras", "collection": "9 mostacillas", "symbol": "△", "description": "Diseño geométrico tejido con 9 mostacillas Miyuki.", "variants": [("Con nudo", 35000), ("Con terminación", 40000)]},
    {"id": "millos-7", "name": "Manilla Millos", "category": "pulseras", "collection": "7 mostacillas", "symbol": "✧", "description": "Diseño tejido con 7 mostacillas Miyuki.", "variants": [("Con nudo", 30000), ("Con terminación", 35000)]},
    {"id": "delica-7", "name": "Manilla Delica", "category": "pulseras", "collection": "7 mostacillas", "symbol": "◇", "description": "Delicadas cuentas Miyuki en un tejido de 7 mostacillas.", "photos": ["manilla-delica-1.jpg", "manilla-delica-2.jpg", "manilla-delica-3.jpg"], "variants": [("Con nudo", 30000), ("Con terminación", 35000)]},
    {"id": "love-7", "name": "Manilla Love", "category": "pulseras", "collection": "7 mostacillas", "symbol": "♡", "description": "Un diseño hecho a mano para llevar cerca.", "variants": [("Con nudo", 30000), ("Con terminación", 35000)]},
    {"id": "tauro-7", "name": "Manilla Zodiaco Tauro", "category": "pulseras", "collection": "7 mostacillas · zodiaco", "zodiac": "tauro", "symbol": "♉", "description": "Pulsera zodiacal inspirada en el signo de Tauro.", "variants": [("Con nudo", 30000), ("Con terminación", 35000)]},
    {"id": "escorpio-7", "name": "Manilla Zodiaco Escorpio", "category": "pulseras", "collection": "7 mostacillas · zodiaco", "zodiac": "escorpio", "symbol": "♏", "description": "Pulsera zodiacal inspirada en el signo de Escorpio.", "variants": [("Con nudo", 30000), ("Con terminación", 35000)]},
    {"id": "leo-7", "name": "Manilla Zodiaco Leo", "category": "pulseras", "collection": "7 mostacillas · zodiaco", "zodiac": "leo", "symbol": "♌", "description": "Pulsera zodiacal inspirada en el signo de Leo.", "variants": [("Con nudo", 30000), ("Con terminación", 35000)]},
    {"id": "geminis-7", "name": "Manilla Zodiaco Géminis", "category": "pulseras", "collection": "7 mostacillas · zodiaco", "zodiac": "geminis", "symbol": "♊", "description": "Pulsera zodiacal inspirada en el signo de Géminis.", "variants": [("Con nudo", 30000), ("Con terminación", 35000)]},
    {"id": "capricornio-7", "name": "Manilla Zodiaco Capricornio", "category": "pulseras", "collection": "7 mostacillas · zodiaco", "zodiac": "capricornio", "symbol": "♑", "description": "Pulsera zodiacal inspirada en el signo de Capricornio.", "variants": [("Con nudo", 30000), ("Con terminación", 35000)]},
    {"id": "libra-7", "name": "Manilla Zodiaco Libra", "category": "pulseras", "collection": "7 mostacillas · zodiaco", "zodiac": "libra", "symbol": "♎", "description": "Pulsera zodiacal inspirada en el signo de Libra.", "variants": [("Con nudo", 30000), ("Con terminación", 35000)]},
    {"id": "manilla-42", "name": "Manilla 42", "category": "pulseras", "collection": "7 mostacillas", "symbol": "✦", "description": "Diseño tejido a mano con cuentas Miyuki.", "variants": [("Con nudo", 30000), ("Con terminación", 35000)]},
    {"id": "glori-5", "name": "Manilla Glori", "category": "pulseras", "collection": "5 mostacillas", "symbol": "✿", "description": "Diseño artesanal tejido con 5 mostacillas Miyuki.", "variants": [("Con nudo", 25000), ("Con terminación", 30000)]},
    {"id": "colombia-5", "name": "Manilla Colombia", "category": "pulseras", "collection": "5 mostacillas", "symbol": "✺", "description": "Diseño tejido con cuentas Miyuki en colores vivos.", "photos": ["manilla-colombia-1.jpg", "manilla-colombia-2.jpg", "manilla-colombia-3.jpg", "manilla-colombia-4.jpg"], "variants": [("Con nudo", 25000), ("Con terminación", 30000)]},
    {"id": "delica-5", "name": "Manilla Delica", "category": "pulseras", "collection": "5 mostacillas", "symbol": "◇", "description": "Cuentas Miyuki Delica en una pieza delicada y ligera.", "variants": [("Con nudo", 25000), ("Con terminación", 30000)]},
    {"id": "llavero-pinguino", "name": "Pingüino + Corazones", "category": "llaveros", "collection": "Llavero", "symbol": "♡", "description": "Un detalle tejido con cuentas Miyuki y corazón.", "price": 20000},
    {"id": "llavero-mariposa", "name": "Mariposa + Girasoles", "category": "llaveros", "collection": "Llavero", "symbol": "✿", "description": "Mariposa y girasoles en un diseño hecho a mano.", "price": 20000},
    {"id": "llavero-girasol", "name": "Girasol + Insectos", "category": "llaveros", "collection": "Llavero", "symbol": "✺", "description": "Un pequeño jardín para llevar contigo.", "price": 20000},
    {"id": "llavero-princesa", "name": "Princesa Grumosa", "category": "llaveros", "collection": "Llavero", "symbol": "✧", "description": "Llavero artesanal decorado con mostacillas Miyuki.", "price": 20000},
    {"id": "colgante-dos-gatos", "name": "Dos Gatos", "category": "colgantes", "collection": "Colgante para celular", "symbol": "☾", "description": "Un par de gatos tejidos para adornar tu celular.", "price": 15054},
    {"id": "colgante-gato", "name": "Gato Cabeza", "category": "colgantes", "collection": "Colgante para celular", "symbol": "猫", "description": "Un pequeño compañero hecho con cuentas Miyuki.", "price": 14847},
    {"id": "prendedor-gorro-rojo", "name": "Gorro Navidad Rojo y Verde", "category": "prendedores", "collection": "Prendedor", "symbol": "✳", "description": "Prendedor festivo elaborado con mostacillas Miyuki.", "price": 18504},
    {"id": "prendedor-gorro", "name": "Gorro Navideño", "category": "prendedores", "collection": "Prendedor", "symbol": "❋", "description": "Un detalle navideño tejido a mano.", "price": 14254},
]
PRODUCTS_BY_ID = {product["id"]: product for product in PRODUCTS}


def format_price(value: int) -> str:
    return f"${value:,.0f}".replace(",", ".")


def image_data_uri(path: Path) -> str:
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    suffix = path.suffix.lower().lstrip(".")
    return f"data:image/{suffix};base64,{encoded}"


def add_to_cart(product: dict, variant_label: str, price: int) -> None:
    key = f"{product['id']}::{variant_label}"
    cart = st.session_state.cart
    st.session_state.last_confirmation = None
    if key in cart:
        cart[key]["quantity"] += 1
    else:
        cart[key] = {
            "product_id": product["id"],
            "name": product["name"],
            "collection": product["collection"],
            "variant": variant_label,
            "price": price,
            "quantity": 1,
        }


def recommendation_profile(product: dict) -> tuple[str, str]:
    name = product["name"].casefold()
    category = product["category"]
    if any(word in name for word in ("arcoíris", "colombia", "millos", "girasol", "mariposa", "pingüino")):
        style = "colorido"
    elif "zodiaco" in name or category in ("prendedores", "colgantes"):
        style = "elegante"
    else:
        style = "minimalista"

    if category in ("llaveros", "colgantes"):
        occasion = "regalo"
    elif category == "prendedores" or "zodiaco" in name or "fiesta" in name:
        occasion = "fiesta"
    else:
        occasion = "diario"
    return style, occasion


def product_recipe(product: dict, variant: str) -> dict[str, int]:
    category = product["category"]
    name = product["name"].casefold()
    if category == "pulseras":
        bead_type = "delica" if "delica" in name else "rocalla"
        count_match = re.search(r"\d+", product["collection"])
        bead_count = int(count_match.group()) if count_match else 7
        recipe = {bead_type: max(2, round(bead_count * 0.35)), "hilo": 2}
        if variant == "Con terminación":
            recipe["cierre"] = 1
        return recipe
    if category == "llaveros":
        return {"delica": 7, "rocalla": 2, "hilo": 4, "dije": 1}
    if category == "colgantes":
        return {"delica": 4, "rocalla": 2, "hilo": 3, "dije": 1}
    return {"rocalla": 4, "hilo": 2, "cristal": 2}


def product_hours(product: dict) -> float:
    if product["category"] == "pulseras":
        count_match = re.search(r"\d+", product["collection"])
        bead_count = int(count_match.group()) if count_match else 7
        return 1.0 + bead_count / 10
    return {
        "llaveros": 1.5,
        "colgantes": 1.0,
        "prendedores": 1.25,
    }[product["category"]]


def order_requirements() -> dict[str, int]:
    required: dict[str, int] = {}
    for key, item in st.session_state.cart.items():
        product_id = item.get("product_id", key.split("::", 1)[0])
        product = PRODUCTS_BY_ID.get(product_id)
        if product is None:
            continue
        for material, amount in product_recipe(product, item["variant"]).items():
            required[material] = required.get(material, 0) + amount * item["quantity"]
    return required


def quote_totals() -> dict[str, float | int]:
    cart = st.session_state.cart
    units = sum(item["quantity"] for item in cart.values())
    subtotal = sum(item["price"] * item["quantity"] for item in cart.values())
    discount_rate = 0.15 if units >= 10 else 0.10 if units >= 5 else 0.05 if units >= 3 else 0
    discount = round(subtotal * discount_rate)
    taxable_amount = subtotal - discount
    tax = round(taxable_amount * IVA_RATE)
    return {
        "units": units,
        "subtotal": subtotal,
        "discount_rate": discount_rate,
        "discount": discount,
        "tax": tax,
        "total": taxable_amount + tax,
    }


def apply_zodiac_selection() -> None:
    sign = st.session_state.selected_sign
    if sign == "Selecciona un signo":
        st.session_state.zodiac_message = "Elige un signo para encontrar tu diseño."
        return

    st.session_state.zodiac_filter = ZODIAC_SIGNS[sign][0]
    st.session_state.category_filter = "Todos"
    st.session_state.zodiac_message = f"Encontramos la pulsera de {sign}."


def render_styles() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&display=swap');
        :root { --ink:#173e38; --green:#17685d; --aqua:#20bda7; --mint:#daf4e9; --soft:#f1faf5; }
        html, body, [class*="css"] { font-family:'DM Sans',sans-serif; }
        .stApp { background:linear-gradient(180deg,#e1f6ee 0,#f1faf5 380px,#f1faf5 100%); color:var(--ink); }
        [data-testid="stHeader"] { background:rgba(225,246,238,.82); }
        .block-container { max-width:1320px; padding-top:1.6rem; padding-bottom:3rem; }
        [data-testid="stToolbar"] { right:1rem; }
        h1,h2,h3 { color:var(--ink); font-family:'Playfair Display',Georgia,serif !important; }
        h2 { font-size:clamp(2rem,4vw,3.2rem) !important; }
        a { color:#17685d !important; }
        [data-testid="stTabs"] [data-testid="stTab"][role="tab"] { color:#17685d !important; opacity:1 !important; font-weight:600; }
        [data-testid="stTabs"] [data-testid="stTab"][role="tab"] [data-testid="stMarkdownContainer"], [data-testid="stTabs"] [data-testid="stTab"][role="tab"] p { color:inherit !important; opacity:1 !important; }
        [data-testid="stTabs"] [data-testid="stTab"][role="tab"][aria-selected="true"] { color:#123e38 !important; background:#daf4e9 !important; }
        [data-testid="stTabs"] [data-testid="stTab"][role="tab"]:focus-visible { outline:2px solid #17685d !important; outline-offset:2px; }
        [data-testid="stRadio"] label[data-testid="stRadioOption"] { color:#173e38 !important; opacity:1 !important; }
        [data-testid="stRadio"] label[data-testid="stRadioOption"] p,
        [data-testid="stRadio"] label[data-testid="stRadioOption"] span { color:#173e38 !important; opacity:1 !important; }
        [data-testid="stRadio"] label[data-testid="stRadioOption"][data-selected="true"] { color:#123e38 !important; font-weight:600; }
        [data-testid="stRadio"] div[role="radiogroup"] label[data-testid="stRadioOption"] { background-color:transparent; }
        .hero-panel { position:relative; display:grid; grid-template-columns:1.05fr .95fr; align-items:center; gap:2rem; min-height:380px; margin:.4rem 0 1.3rem; padding:2.4rem clamp(1.3rem,5vw,4.2rem); overflow:hidden; border:1px solid rgba(32,153,130,.18); border-radius:20px; background:radial-gradient(ellipse at 74% 44%,rgba(94,212,189,.46),transparent 39%),radial-gradient(ellipse at 7% 94%,rgba(122,221,193,.31),transparent 36%),linear-gradient(120deg,#d9f4e9,#bfece0 58%,#e6f7ec); box-shadow:0 12px 40px rgba(27,113,91,.08); }
        .hero-kicker { color:#197566; font-size:.72rem; font-weight:700; letter-spacing:.16em; text-transform:uppercase; }
        .hero-title { max-width:600px; margin:.8rem 0; color:#123e38; font:400 clamp(2.7rem,5vw,5rem)/1.02 'Playfair Display',Georgia,serif; letter-spacing:-.04em; }
        .hero-title em { color:#329888; }
        .hero-description { max-width:475px; color:#53756b; line-height:1.8; }
        .hero-caption { margin-top:.7rem; color:#387563; font:italic .86rem 'Playfair Display',Georgia,serif; text-align:center; }
        .hero-art { position:relative; display:grid; min-height:320px; place-items:center; }
        .hero-logo { position:relative; z-index:1; width:min(280px,67%); aspect-ratio:1; object-fit:cover; border:7px solid rgba(255,255,255,.82); border-radius:50%; box-shadow:0 16px 48px rgba(21,61,53,.17); }
        .hero-sakura { position:absolute; z-index:2; right:-8%; bottom:-3%; width:min(350px,76%); }
        .hero-orbit { position:absolute; width:min(360px,94%); aspect-ratio:1; border:1px solid rgba(32,157,135,.4); border-radius:50%; }
        .hero-orbit:before { position:absolute; inset:-17px; content:''; border:1px dashed rgba(23,104,93,.22); border-radius:50%; }
        .section-kicker { color:#238271; font-size:.69rem; font-weight:700; letter-spacing:.17em; text-transform:uppercase; }
        .promise-strip { margin:.6rem 0 2.4rem; padding:.9rem 1rem; border:1px solid rgba(32,157,135,.13); border-radius:10px; background:linear-gradient(90deg,#a8e8d8,#d4f4e6 50%,#a8e8d8); color:#155e52; font:1rem 'Playfair Display',Georgia,serif; text-align:center; }
        .product-card { min-height:100%; padding:0 0 .45rem; }
        .product-tag { display:inline-block; margin:.3rem 0 .35rem; padding:.24rem .55rem; border-radius:2rem; background:#daf4e9; color:#17685d; font-size:.64rem; letter-spacing:.08em; text-transform:uppercase; }
        .product-collection { margin:0; color:#329888; font-size:.65rem; font-weight:700; letter-spacing:.11em; text-transform:uppercase; }
        .product-description { min-height:2.8rem; color:#71847c; font-size:.8rem; line-height:1.6; }
        .product-fallback { display:grid; min-height:190px; place-items:center; border-radius:8px; background:radial-gradient(circle,#fff 0 25%,transparent 26%),linear-gradient(145deg,#c5f0e5,#8bdac8 58%,#e0f6e8); color:#237b6d; font:3.3rem 'Playfair Display',Georgia,serif; }
        .wheel-wrap { display:grid; place-items:center; padding:1rem; border:1px solid rgba(218,248,232,.28); border-radius:16px; background:radial-gradient(ellipse at 50% 45%,rgba(113,231,205,.27),transparent 60%),rgba(14,101,87,.16); }
        .wheel-wrap svg { width:min(100%,360px); height:auto; }
        .wheel-wrap .outer,.wheel-wrap .ring,.wheel-wrap .center { fill:rgba(12,91,79,.16); stroke:rgba(206,250,229,.75); stroke-width:1.2; }
        .wheel-wrap .ring-inner { stroke:rgba(199,245,223,.49); stroke-dasharray:2 5; }
        .wheel-wrap .center { fill:rgba(203,244,223,.14); }
        .wheel-wrap .spokes { fill:none; stroke:rgba(205,244,223,.42); stroke-width:1; }
        .wheel-wrap .signs { fill:#e1f8eb; font:22px 'Segoe UI Symbol',serif; text-anchor:middle; }
        .wheel-wrap .stars { fill:#b6efda; }
        .wheel-wrap .moon { fill:#a9e8d2; stroke:#dbf6e7; }
        .wheel-wrap .torii { fill:none; stroke:#e3f7e9; stroke-linecap:round; stroke-linejoin:round; stroke-width:3; }
        .wheel-wrap .caption { fill:#c6efdc; font:8px 'DM Sans',sans-serif; letter-spacing:2px; text-anchor:middle; }
        div.stButton > button { border-radius:6px; border:1px solid #17685d; background:#17685d; color:#fff; font-weight:600; }
        div.stButton > button:hover { border-color:#20bda7; background:#20bda7; color:#fff; }
        [data-testid="stMetric"] { padding:.85rem; border:1px solid rgba(32,157,135,.18); border-radius:9px; background:#fbfffc; }
        .footer-note { padding:1rem 0 .1rem; border-top:1px solid rgba(32,157,135,.2); color:#53756b; font:italic .9rem 'Playfair Display',Georgia,serif; text-align:center; }
        @media(max-width:700px) { .hero-panel { grid-template-columns:1fr; gap:.3rem; padding:1.6rem 1.2rem; } .hero-art { min-height:250px; } .hero-logo { width:min(215px,62%); } .hero-sakura { width:min(280px,78%); } }
        </style>
        """,
        unsafe_allow_html=True,
    )


def zodiac_wheel() -> str:
    signs = [
        ("♈︎", 210, 59), ("♉︎", 286, 80), ("♊︎", 341, 135),
        ("♋︎", 361, 218), ("♌︎", 332, 300), ("♍︎", 267, 352),
        ("♎︎", 210, 375), ("♏︎", 133, 352), ("♐︎", 78, 300),
        ("♑︎", 58, 218), ("♒︎", 83, 135), ("♓︎", 144, 80),
    ]
    sign_labels = "".join(
        f'<text x="{x}" y="{y}">{sign}</text>' for sign, x, y in signs
    )
    return f"""
    <svg viewBox="0 0 420 420" role="img" aria-label="Rueda con los doce signos del zodiaco">
      <circle class="outer" cx="210" cy="210" r="190"/>
      <circle class="ring" cx="210" cy="210" r="165"/>
      <circle class="ring ring-inner" cx="210" cy="210" r="113"/>
      <circle class="center" cx="210" cy="210" r="68"/>
      <g class="spokes"><path d="M210 20v77M210 323v77M20 210h77M323 210h77M75.65 75.65l54.45 54.45m159.8 159.8 54.45 54.45M344.35 75.65l-54.45 54.45m-159.8 159.8-54.45 54.45"/></g>
      <g class="signs">{sign_labels}</g>
      <g class="stars"><path d="m210 161 4 11 11 4-11 4-4 11-4-11-11-4 11-4zm0 58 3 8 8 3-8 3-3 8-3-8-8-3 8-3z"/><circle cx="181" cy="196" r="2"/><circle cx="239" cy="197" r="2"/><circle cx="189" cy="228" r="1.5"/><circle cx="232" cy="228" r="1.5"/></g>
      <g class="torii"><path d="M183 192h54l-5 5h-44l-5-5Zm6 9h42l-4 5h-34l-4-5Zm4 7v24m29-24v24m-29-7h29"/></g>
      <path class="moon" d="M253 139a25 25 0 1 1-28-37 21 21 0 0 0 28 37Z"/>
      <text class="caption" x="210" y="410">UN PEQUEÑO UNIVERSO</text>
    </svg>
    """


def product_price(product: dict, variant_index: int = 0) -> tuple[str, int]:
    variants = product.get("variants")
    if variants:
        return variants[variant_index]
    return "Diseño único", product["price"]


def render_product(product: dict, index: int) -> None:
    with st.container(border=True):
        photos = product.get("photos", [])
        if photos:
            photo_index = 0
            if len(photos) > 1:
                photo_index = st.radio(
                    "Foto del diseño",
                    options=range(len(photos)),
                    format_func=lambda value: f"Vista {value + 1}",
                    horizontal=True,
                    label_visibility="collapsed",
                    key=f"photo-{product['id']}",
                )
            st.image(ASSETS / "productos" / photos[photo_index], width="stretch")
        else:
            st.markdown(
                f'<div class="product-fallback">{product["symbol"]}</div>',
                unsafe_allow_html=True,
            )

        st.markdown(
            f'<span class="product-tag">{product["category"].title()}</span>'
            f'<p class="product-collection">{product["collection"]}</p>'
            f'<h3>{product["name"]}</h3>'
            f'<p class="product-description">{product["description"]}</p>',
            unsafe_allow_html=True,
        )

        variants = product.get("variants")
        variant_index = 0
        if variants:
            variant_index = st.selectbox(
                "Acabado",
                options=range(len(variants)),
                format_func=lambda value: (
                    f"{variants[value][0]} · {format_price(variants[value][1])}"
                ),
                key=f"variant-{product['id']}",
            )
        variant_label, price = product_price(product, variant_index)
        st.markdown(f"**{format_price(price)}**")
        if st.button("＋ Agregar", key=f"add-{product['id']}", width="stretch"):
            add_to_cart(product, variant_label, price)
            st.toast(f"{product['name']} se agregó a tu pedido.")


def render_cart() -> None:
    st.subheader("Tu pedido, con intención")
    cart = st.session_state.cart
    totals = quote_totals()
    metric_quantity, metric_total = st.columns(2)
    metric_quantity.metric("Piezas", totals["units"])
    metric_total.metric("Total estimado", format_price(totals["total"]))

    if not cart:
        st.info("Tu pedido comienza con una intención. Agrega tus diseños favoritos para ver aquí el resumen.")
        return

    for key, item in list(cart.items()):
        name_col, quantity_col, remove_col = st.columns([4, 1, 1])
        with name_col:
            variant = "" if item["variant"] == "Diseño único" else f" · {item['variant']}"
            st.markdown(
                f"**{item['name']}**  \n"
                f"<small>{item['collection']}{variant} · "
                f"{format_price(item['price'])} c/u</small>",
                unsafe_allow_html=True,
            )
        with quantity_col:
            st.write(f"× {item['quantity']}")
        with remove_col:
            if st.button("Quitar", key=f"remove-{key}"):
                del cart[key]
                st.rerun()

    st.divider()
    st.write(f"Subtotal: **{format_price(totals['subtotal'])}**")
    if totals["discount"]:
        st.write(
            f"Descuento por volumen ({totals['discount_rate']:.0%}): "
            f"**−{format_price(totals['discount'])}**"
        )
    st.write(f"IVA (19%): **{format_price(totals['tax'])}**")
    st.subheader(f"Total estimado: {format_price(totals['total'])}")
    st.caption("Precios y cálculo de IVA de referencia; envío por cotizar.")

    lines = [
        f"- {item['quantity']} x {item['name']} ({item['variant']}): "
        f"{format_price(item['price'] * item['quantity'])}"
        for item in cart.values()
    ]
    order_text = "\n".join(
        [
            "Cotización estimada · Miyuki Accesorios",
            *lines,
            f"Subtotal: {format_price(totals['subtotal'])}",
            f"Descuento: {format_price(totals['discount'])}",
            f"IVA (19%): {format_price(totals['tax'])}",
            f"Total estimado: {format_price(totals['total'])}",
            "Envío por cotizar. Valores sujetos a confirmación.",
        ]
    )
    download_col, clear_col = st.columns(2)
    with download_col:
        st.download_button(
            "Descargar cotización",
            data=order_text,
            file_name="cotizacion-miyuki.txt",
            mime="text/plain",
            width="stretch",
        )
    with clear_col:
        if st.button("Vaciar pedido", width="stretch"):
            cart.clear()
            st.session_state.last_confirmation = None
            st.rerun()


def render_catalog() -> None:
    heading_col, search_col = st.columns([1.3, 0.7], vertical_alignment="bottom")
    with heading_col:
        st.markdown('<p class="section-kicker">Colección Miyuki</p>', unsafe_allow_html=True)
        st.header("Encuentra tu amuleto")
        st.caption("Piezas inspiradas en los colores, símbolos y pequeños momentos que hacen único tu universo.")
    with search_col:
        search = st.text_input("Buscar un diseño", placeholder="Nombre, estilo o categoría…")

    filter_col, count_col = st.columns([0.75, 0.25], vertical_alignment="center")
    with filter_col:
        category = st.radio(
            "Filtrar por categoría",
            options=list(CATEGORIES),
            horizontal=True,
            key="category_filter",
        )
    zodiac_filter = st.session_state.zodiac_filter
    filtered_products = [
        product
        for product in PRODUCTS
        if (CATEGORIES[category] == "todos" or product["category"] == CATEGORIES[category])
        and (not zodiac_filter or product.get("zodiac") == zodiac_filter)
        and search.casefold()
        in f"{product['name']} {product['collection']} {product['description']}".casefold()
    ]
    with count_col:
        count = len(filtered_products)
        design_label = "diseño disponible" if count == 1 else "diseños disponibles"
        st.caption(f"{count} {design_label}")
    if zodiac_filter and st.button("Quitar filtro zodiacal"):
        st.session_state.zodiac_filter = ""
        st.rerun()
    if filtered_products:
        columns = st.columns(3)
        for index, product in enumerate(filtered_products):
            with columns[index % len(columns)]:
                render_product(product, index)
    else:
        st.info("No encontramos diseños con esos filtros. Prueba otra búsqueda o categoría.")

    st.divider()
    zodiac_col, wheel_col = st.columns([1.2, 0.8], gap="large", vertical_alignment="center")
    with zodiac_col:
        st.markdown('<p class="section-kicker">Una guía entre estrellas</p>', unsafe_allow_html=True)
        st.header("¿Qué signo acompaña tu camino?")
        st.write(
            "En la colección hay pulseras zodiacales tejidas con cuentas Miyuki. "
            "Elige uno de los diseños disponibles y encuentra el tuyo."
        )
        st.selectbox(
            "Elige tu signo",
            options=["Selecciona un signo", *ZODIAC_SIGNS],
            key="selected_sign",
        )
        st.button("Ver mi pulsera zodiacal", on_click=apply_zodiac_selection)
        if st.session_state.get("zodiac_message"):
            st.caption(st.session_state.zodiac_message)
    with wheel_col:
        st.markdown(
            f'<div class="wheel-wrap">{zodiac_wheel()}</div>',
            unsafe_allow_html=True,
        )


def render_add_to_order() -> None:
    st.subheader("Agregar productos al pedido")
    product = st.selectbox("Diseño", PRODUCTS, format_func=lambda item: item["name"])
    variant_index = 0
    variants = product.get("variants")
    if variants:
        variant_index = st.selectbox(
            "Acabado",
            options=range(len(variants)),
            format_func=lambda value: (
                f"{variants[value][0]} · {format_price(variants[value][1])}"
            ),
            key="order_variant",
        )
    variant, price = product_price(product, variant_index)
    quantity = st.number_input("Cantidad", min_value=1, max_value=100, value=1, step=1)
    st.write(f"Precio unitario: **{format_price(price)}**")
    if st.button("Agregar al pedido", type="primary"):
        for _ in range(quantity):
            add_to_cart(product, variant, price)
        st.session_state.last_confirmation = None
        st.success(f"{quantity} × {product['name']} agregado(s) al pedido.")


def render_recommendations() -> None:
    st.subheader("Recomendación personalizada")
    st.caption("El estilo y la ocasión se estimaron a partir del nombre y tipo de cada diseño.")
    style_col, occasion_col = st.columns(2)
    with style_col:
        style = st.selectbox(
            "¿Qué estilo prefieres?", STYLE_OPTIONS, key="recommendation_style"
        )
    with occasion_col:
        occasion = st.selectbox(
            "¿Para qué ocasión?", OCCASION_OPTIONS, key="recommendation_occasion"
        )
    budget = st.number_input(
        "Presupuesto máximo por pieza (COP)",
        min_value=5000,
        max_value=500000,
        value=65000,
        step=5000,
        key="recommendation_budget",
    )

    recommendations = []
    for product in PRODUCTS:
        product_style, product_occasion = recommendation_profile(product)
        _, price = product_price(product)
        if price > budget:
            continue
        score = 2 * (product_style == style) + (product_occasion == occasion)
        recommendations.append((score, price, product))
    recommendations.sort(key=lambda result: (-result[0], result[1], result[2]["name"]))
    if not recommendations:
        st.info("No encontramos diseños dentro de ese presupuesto. Prueba con un monto mayor.")
        return

    st.write(f"Diseños que caben en tu presupuesto: **{len(recommendations)}**")
    best_score = recommendations[0][0]
    for score, price, product in recommendations[:8]:
        with st.container(border=True):
            style_label, occasion_label = recommendation_profile(product)
            match = "Ideal para ti" if score == 3 else "Coincide con tu estilo" if score == 2 else "También puede gustarte"
            st.markdown(f"**{product['name']}** · {match}")
            st.caption(
                f"{style_label.title()} · Para {occasion_label} · "
                f"{format_price(price)}"
            )
            if product.get("variants"):
                variant, _ = product_price(product)
            else:
                variant = "Diseño único"
            if st.button("＋ Agregar recomendación", key=f"recommend-{product['id']}"):
                add_to_cart(product, variant, price)
                st.toast(f"{product['name']} se agregó a tu pedido.")
    if best_score == 0:
        st.caption("No hay coincidencias exactas, pero mostramos opciones dentro de tu presupuesto.")


def render_inventory() -> None:
    st.subheader("Inventario de materiales")
    st.info(
        "Inventario de demostración: los stocks y costos iniciales son valores de ejemplo "
        "y solo se guardan durante esta sesión."
    )
    rows = []
    for material in st.session_state.inventory.values():
        rows.append(
            {
                "Material": material["name"],
                "Stock": material["stock"],
                "Unidad": material["unit"],
                "Costo estimado": format_price(material["cost"]),
                "Estado": "Stock bajo" if material["stock"] < 20 else "Disponible",
            }
        )
    st.dataframe(rows, hide_index=True, width="stretch")


def render_production_plan() -> None:
    st.subheader("Verificar materiales y planificar producción")
    cart = st.session_state.cart
    if not cart:
        st.info("Agrega productos al pedido para consultar los materiales y la producción.")
        return

    required = order_requirements()
    inventory = st.session_state.inventory
    shortages = {
        material: max(0, quantity - inventory[material]["stock"])
        for material, quantity in required.items()
    }
    shortages = {material: quantity for material, quantity in shortages.items() if quantity > 0}
    rows = [
        {
            "Material": inventory[material]["name"],
            "Necesario": quantity,
            "Disponible": inventory[material]["stock"],
            "Faltante": max(0, quantity - inventory[material]["stock"]),
            "Unidad": inventory[material]["unit"],
        }
        for material, quantity in required.items()
    ]
    st.dataframe(rows, hide_index=True, width="stretch")

    hours = sum(
        product_hours(PRODUCTS_BY_ID[item.get("product_id", key.split("::", 1)[0])])
        * item["quantity"]
        for key, item in cart.items()
    )
    production_days = ceil(hours / HOURS_PER_DAY)
    restock_cost = sum(
        quantity * inventory[material]["cost"]
        for material, quantity in shortages.items()
    )
    delivery_days = production_days + (RESTOCK_DAYS if shortages else 0)
    delivery_date = date.today() + timedelta(days=delivery_days)
    metric_hours, metric_days, metric_delivery = st.columns(3)
    metric_hours.metric("Trabajo estimado", f"{hours:.1f} h")
    metric_days.metric("Días de producción", production_days)
    metric_delivery.metric("Entrega estimada", delivery_date.strftime("%d/%m/%Y"))
    st.caption(f"Estimación calculada con {HOURS_PER_DAY} horas de trabajo al día.")
    if shortages:
        st.warning(
            f"Faltan materiales para completar el pedido. Compra estimada: "
            f"{format_price(restock_cost)}. Se agregan {RESTOCK_DAYS} días para reabastecer."
        )
    else:
        st.success("Hay materiales suficientes para producir este pedido.")
    st.caption("Recetas y tiempos inventados como referencia; no sustituyen una ficha técnica real.")


def render_confirmation() -> None:
    st.subheader("Confirmar pedido")
    cart = st.session_state.cart
    if not cart:
        confirmation = st.session_state.get("last_confirmation")
        if confirmation:
            st.success(
                f"Pedido confirmado. Total estimado: {format_price(confirmation['total'])}. "
                "El inventario de demostración se actualizó."
            )
        else:
            st.info("Tu pedido está vacío. Agrega productos antes de confirmar.")
        return

    totals = quote_totals()
    st.write(f"Piezas en el pedido: **{totals['units']}**")
    st.write(f"Total estimado con descuento e IVA: **{format_price(totals['total'])}**")
    required = order_requirements()
    inventory = st.session_state.inventory
    shortages = {
        material: quantity - inventory[material]["stock"]
        for material, quantity in required.items()
        if quantity > inventory[material]["stock"]
    }
    if shortages:
        st.error("No se puede confirmar hasta reabastecer los materiales faltantes:")
        for material, quantity in shortages.items():
            st.write(f"- {inventory[material]['name']}: faltan {quantity} {inventory[material]['unit']}")
        st.caption("Usa la opción 8 para reabastecer y vuelve a confirmar.")
        return

    st.warning(
        "Al confirmar, se descontarán materiales del inventario de demostración de esta sesión "
        "y se vaciará el pedido."
    )
    if st.button("Confirmar y descontar inventario", type="primary"):
        for material, quantity in required.items():
            inventory[material]["stock"] -= quantity
        st.session_state.last_confirmation = {"total": totals["total"]}
        cart.clear()
        st.rerun()


def render_restock() -> None:
    st.subheader("Reabastecer inventario")
    st.caption("Los cambios aplican solo a tu sesión de demostración.")
    if st.session_state.get("restock_message"):
        st.success(st.session_state.restock_message)
        st.session_state.restock_message = ""
    inventory = st.session_state.inventory
    material_key = st.selectbox(
        "Material",
        options=list(inventory),
        format_func=lambda key: (
            f"{inventory[key]['name']} · stock actual: {inventory[key]['stock']} "
            f"{inventory[key]['unit']}"
        ),
    )
    amount = st.number_input("Cantidad que ingresa", min_value=1, max_value=100000, value=10, step=1)
    if st.button("Registrar reabastecimiento"):
        inventory[material_key]["stock"] += amount
        st.session_state.restock_message = (
            f"Nuevo stock de {inventory[material_key]['name']}: "
            f"{inventory[material_key]['stock']} {inventory[material_key]['unit']}."
        )
        st.rerun()


def render_hero() -> None:
    logo = image_data_uri(ASSETS / "logo-miyuki.png")
    sakura = image_data_uri(ASSETS / "ilustraciones" / "ramo-sakura.svg")
    st.markdown(
        f"""
        <section class="hero-panel">
          <div>
            <div class="hero-kicker">✳ Hecho a mano, con intención</div>
            <h1 class="hero-title">Un pequeño universo <em>en tus manos.</em></h1>
            <p class="hero-description">Accesorios Miyuki tejidos puntada a puntada. Inspiración japonesa, naturaleza y un toque de magia astral para acompañarte cada día.</p>
            <div class="hero-kicker">Pequeños detalles, energía infinita</div>
          </div>
          <div class="hero-art">
            <div class="hero-orbit"></div>
            <img class="hero-logo" src="{logo}" alt="Logo de Miyuki Accesorios">
            <img class="hero-sakura" src="{sakura}" alt="">
          </div>
        </section>
        <div class="promise-strip">和 &nbsp; Inspiración japonesa &nbsp; · &nbsp; ✺ Tejido artesanal &nbsp; · &nbsp; ☾ Detalles con significado</div>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:
    st.set_page_config(
        page_title="Miyuki Accesorios | Amuletos hechos a mano",
        page_icon=str(ASSETS / "logo-miyuki.png"),
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render_styles()
    st.session_state.setdefault("cart", {})
    st.session_state.setdefault("zodiac_filter", "")
    st.session_state.setdefault("inventory", deepcopy(INITIAL_INVENTORY))
    st.session_state.setdefault("last_confirmation", None)
    render_hero()
    st.caption(
        "El catálogo conserva los precios de referencia actuales. "
        "Las recetas, costos de materiales, horas y stocks son datos inventados para demostración."
    )

    tabs = st.tabs(
        [
            "1. Ver catálogo",
            "2. Ver inventario",
            "3. Recomendar accesorios",
            "4. Agregar al pedido",
            "5. Ver cotización",
            "6. Planificar producción",
            "7. Confirmar pedido",
            "8. Reabastecer",
        ]
    )
    with tabs[0]:
        render_catalog()
    with tabs[1]:
        render_inventory()
    with tabs[2]:
        render_recommendations()
    with tabs[3]:
        render_add_to_order()
    with tabs[4]:
        render_cart()
    with tabs[5]:
        render_production_plan()
    with tabs[6]:
        render_confirmation()
    with tabs[7]:
        render_restock()

    st.divider()
    st.markdown('<p class="section-kicker">Nuestra esencia</p>', unsafe_allow_html=True)
    st.header("El arte de crear despacito.")
    st.write(
        "Cada diseño nace de la paciencia de tejer pequeñas cuentas y convertirlas "
        "en algo que puedas llevar contigo. Color, intención y un pedacito de cielo, hecho a mano."
    )
    st.markdown(
        '<p class="footer-note">Miyuki Accesorios · Hecho a mano con calma, para brillar a tu manera.</p>',
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
