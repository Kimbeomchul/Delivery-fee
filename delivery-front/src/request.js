const baseURL = "http://localhost:8000/api/v1";
//  baseURL: `${SERVER_ADDRESS}`

const request = async (action, method, data = null) => {
    if (data !== null) {
        data = JSON.stringify(data);
    }
    const response = await fetch(`${baseURL}${action}`, {
        method: method,
        headers: {
            "Content-Type": "application/json",
        },
        body: data,
    });
    return {
        status: response.status,
        data: await response.json(),
    };
};

export default request;
