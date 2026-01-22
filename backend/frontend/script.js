async function predictPrice() {

    const data = {
        Present_Price: parseFloat(document.getElementById("present_price").value),
        Kms_Driven: parseInt(document.getElementById("kms_driven").value),
        Fuel_Type: document.getElementById("fuel_type").value,
        Seller_Type: document.getElementById("seller_type").value,
        Transmission: document.getElementById("transmission").value,
        Owner: parseInt(document.getElementById("owner").value),
        Car_Age: parseInt(document.getElementById("car_age").value)
    };

    const response = await fetch("https://car-price-prediction-49m5.onrender.com/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    document.getElementById("result").innerText =
        "Predicted Price: ₹ " + result.predicted_price + " Lakhs";
}