import store from "./store";

const baseURL = "http://localhost:8000/api/v1";
//  baseURL: `${SERVER_ADDRESS}`

const InfiniteRequest = async ($state, action, page = null, dispatch) => {
    if (!page) {
        $state.complete();
        return;
    }

    await fetch(`${baseURL}${action}?page=` + page, {
        method: "get",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${store.state.userInfo.access_token}`,
        },
    })
        .then((resp) => {
            return resp.json();
        })
        .then((data) => {
            setTimeout(() => {
                if (data["results"]) {
                    data["results"]["infinite"] = true;
                    store.dispatch(dispatch, data["results"]);
                    $state.loaded();
                    page += 1;

                    if (!data["next"]) {
                        $state.complete();
                    }
                } else {
                    // 끝 지정(No more data)
                    $state.complete();
                }
            }, 500);
        })
        .catch((err) => {
            console.error(err);
        });
};

export default InfiniteRequest;
