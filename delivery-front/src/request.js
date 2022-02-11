const baseURL = "http://localhost:8000/api/v1";
//  baseURL: `${SERVER_ADDRESS}`

const request = async (action, method, data = null) => {
    // eslint-disable-next-line no-unused-vars
    if (data !== null) {
        data = JSON.stringify(data);
    }
    let response = await fetch(`${baseURL}${action}`, {
        method: method,
        headers: {
            "Content-Type": "application/json",
        },
        body: data,
    });
    return await response.json();
};

export default request;
