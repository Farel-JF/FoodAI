document.getElementById('ai-form').addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent form submission

  const goal = document.getElementById('goal').value;
  const diet = document.getElementById('diet').value;
  const recommendationsDiv = document.getElementById('recommendations');

  // Clear previous recommendations
  recommendationsDiv.innerHTML = '';

  // Sample recommendations based on user input (this could be replaced with real logic or API calls)
  let recommendations = `<h3>Your Recommendations:</h3><ul>`;

  if (goal === 'gain') {
      recommendations += `<li>High-calorie Protein Powder</li>`;
      recommendations += `<li>Nut Butter</li>`;
  } else if (goal === 'lose') {
      recommendations += `<li>Low-Calorie Meal Plan</li>`;
      recommendations += `<li>Protein Shakes</li>`;
  } else if (goal === 'maintain') {
      recommendations += `<li>Balanced Meal Kit</li>`;
      recommendations += `<li>Energy Bars</li>`;
  }

  if (diet === 'vegan') {
      recommendations += `<li>Vegan Protein Powder</li>`;
  } else if (diet === 'vegetarian') {
      recommendations += `<li>Vegetarian Meal Prep</li>`;
  } else if (diet === 'omnivore') {
      recommendations += `<li>Mixed Protein Options</li>`;
  }

  recommendations += `</ul>`;
  recommendationsDiv.innerHTML = recommendations;
});
