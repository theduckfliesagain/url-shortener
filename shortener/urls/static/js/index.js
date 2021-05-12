const main = document.querySelector("main");

main.addEventListener('click', (e) => {
    if (e.target.className === "copy-btn") {
        copyURL(e);
    }
})

function copyURL(e) {
    const copyText = e.target.parentElement.textContent.trim();

    navigator.permissions.query({ name: "clipboard-write" }).then(result => {
        if (result.state == "granted" || result.state == "prompt") {
            navigator.clipboard.writeText(copyText);
        }
    });
    // copyText.select();
    // copyText.setSelectionRange(0, 99999); /* For mobile devices */

    // /* Copy the text inside the text field */
    // document.execCommand("copy");

    /* Alert the copied text */
    // alert("Copied the text: " + copyText.value);
}