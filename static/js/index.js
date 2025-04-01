document.addEventListener("DOMContentLoaded", function () {

    window.addEventListener("pageshow", function () {
        const buttons = document.querySelectorAll(".btn-loading");
      
        buttons.forEach((button) => {
          const textSpan = button.querySelector(".btn-text");
          const loadingImg = button.querySelector(".loading-icon");
      
          if (textSpan && textSpan.innerText === "Carregando...") {
            textSpan.innerText = button.dataset.originalText || "Enviar";
          }
      
          if (loadingImg) loadingImg.style.display = "none";
      
          button.disabled = false;
        });
      });

    const forms = document.querySelectorAll("form");

    forms.forEach((form) => {
        form.addEventListener("submit", function (event) {
            const button = form.querySelector(".btn-loading");

            if (button) {
                event.preventDefault();

                const textSpan = button.querySelector(".btn-text");
                const loadingImg = button.querySelector(".loading-icon");

                if (textSpan) textSpan.innerText = "Carregando...";
                if (loadingImg) loadingImg.style.display = "inline";

                button.disabled = true;
                button.classList.add("disabled");

                setTimeout(() => {
                    form.submit();
                }, 2000);
            }
        });
    });

    const redirectButtons = document.querySelectorAll(".btn-loading[data-href]");

    redirectButtons.forEach((button) => {
        button.addEventListener("click", function (event) {
            event.preventDefault();

            const textSpan = button.querySelector(".btn-text");
            const loadingImg = button.querySelector(".loading-icon");
            const targetUrl = button.getAttribute("data-href");

            if (textSpan) textSpan.innerText = "Carregando...";
            if (loadingImg) loadingImg.style.display = "inline";

            button.disabled = true;
            button.classList.add("disabled");

            setTimeout(() => {
                window.location.href = targetUrl;
            }, 2000);
        });
    });
})