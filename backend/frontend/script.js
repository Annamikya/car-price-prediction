document.getElementById('prediction-form').addEventListener('submit', async function(e) {
    e.preventDefault();

    const button = document.getElementById('predict-btn');
    const resultDiv = document.getElementById('result');
    const priceValue = document.getElementById('price-value');

    // Get form data
    const data = {
        Present_Price: parseFloat(document.getElementById("present_price").value),
        Kms_Driven: parseInt(document.getElementById("kms_driven").value),
        Fuel_Type: document.getElementById("fuel_type").value,
        Seller_Type: document.getElementById("seller_type").value,
        Transmission: document.getElementById("transmission").value,
        Owner: parseInt(document.getElementById("owner").value),
        Car_Age: parseInt(document.getElementById("car_age").value)
    };

    // Validate inputs
    if (!data.Present_Price || !data.Kms_Driven || !data.Car_Age || !data.Fuel_Type || !data.Seller_Type || !data.Transmission || data.Owner === undefined) {
        alert('Please fill in all fields');
        return;
    }

    // Show loading
    button.disabled = true;
    button.textContent = 'Predicting...';
    button.classList.add('loading');
    resultDiv.classList.add('hidden');

    try {
        const response = await fetch("/api/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error('Prediction failed');
        }

        const result = await response.json();
        priceValue.textContent = "₹ " + result.predicted_price + " Lakhs";
        resultDiv.classList.remove('hidden');

    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while predicting. Please try again.');
    } finally {
        // Hide loading
        button.disabled = false;
        button.textContent = 'Predict Price';
        button.classList.remove('loading');
    }
});