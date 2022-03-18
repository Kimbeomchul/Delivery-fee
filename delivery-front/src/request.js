import store from "./store";

const baseURL = "http://localhost:8000/api/v1";
//  baseURL: `${SERVER_ADDRESS}`

const request = async (action, method, data = null) => {
    if (data !== null) {
        data = JSON.stringify(data);
    }

    let options = {
        method: method,
        headers: {
            "Content-Type": "application/json",
        },
        body: data,
    };

    // 회원가입 하는 경우는 header에 Authorization 제외
    if (store.state.userInfo && store.state.userInfo.access_token) {
        options.headers["Authorization"] = `Bearer ${store.state.userInfo.access_token}`;
    }

    const response = await fetch(`${baseURL}${action}`, options);
    return {
        status: response.status,
        data: await response.json().catch(() => ({})),
    };
};

export default request;
