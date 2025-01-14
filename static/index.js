const fetchBtn = document.getElementById("fetch-trends-twitter-btn");
const getBtn = document.getElementById("get-trends-db-btn");
const resultcontainer = document.getElementById("result");

fetchBtn.addEventListener('click',(e) => {
    e.preventDefault();
    fetch('/fetch-trends', {
        method: 'GET',
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const trendingData = data.trend;
            const startTime = new Date(trendingData.start_time * 1000).toLocaleString();
            const endTime = new Date(trendingData.end_time * 1000).toLocaleString();
            // const trends = trendingData.trends.map(trend => `<li>${trend}</li>`).join('');
            let trends = '';
            for(let k = 0; k < trendingData.trends.length; k++)
            {
                trends += `<li>trend${k+1}: ${trendingData.trends[k+1]} </li>`
            }
            const ipAddress = trendingData.ipaddress;

            resultcontainer.innerHTML += `
                <h3>Script: </h3>
                <p>Start time of script: ${startTime}</p>
                <p>End time of script: ${endTime}</p>
                <ul>
                    ${trends}
                </ul>
                <p>The IP address used for this query was ${ipAddress}.</p>
            `;
        } else {
            resultcontainer.innerHTML = '<p>Error fetching trends.</p>';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById("result").innerHTML = '<p>Error fetching trends.</p>';
    });
})



getBtn.addEventListener("click", (e) => {
    e.preventDefault();
    fetch('/get-trends', {
        method: 'GET',
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const trends_data = data.trends;

            for(let i = 0; i < trends_data.length ; i++) {
                const trendingData = trends_data[i];
                const startTime = new Date(trendingData.start_time * 1000).toLocaleString();
                const endTime = new Date(trendingData.end_time * 1000).toLocaleString();
                // const trends = trendingData.trends.map(trend => `<li>trend${i+1}: ${trend}</li>`).join('');
                let trends = '';
                for(let k = 0; k < trendingData.trends.length; k++)
                {
                    trends += `<li>trend${k+1}: ${trendingData.trends[k+1]} </li>`
                }
                const ipAddress = trendingData.ipaddress;

                resultcontainer.innerHTML += `
                    <h3>Script - ${i+1}</h3>
                    <p>Start time of script: ${startTime}</p>
                    <p>End time of script: ${endTime}</p>
                    <ul>
                        ${trends}
                    </ul>
                    <p>The IP address used for this query was ${ipAddress}.</p>
                `;
            }   
           
        } else {
            resultcontainer.innerHTML = '<p>Error fetching trends.</p>';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById("result").innerHTML = '<p>Error fetching trends.</p>';
    });
});
