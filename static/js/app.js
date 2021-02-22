const item_datas = document.querySelectorAll(".item_data");
            const delete_option = document.querySelectorAll(".delete_option");
            const option_div = document.querySelector(".delete_container");

            delete_option.forEach((option,id) =>
             {
                option.addEventListener('click', () => 
                {
                    const p = ` <h2>Sure to Delete this Content?</h2>
                                 <p>${item_datas[id].textContent}</p>
                                        <div class="delete_btn_cont">
                                            <button class="cancel_btn" id="cancel_btn">Cancel</button>
                                            <button> <a href="delete/${option.value}">
                                                <i class="fas fa-trash"></i>Delete</a></button>
                                        </div>`;
                    option_div.innerHTML = p;
                    option_div.style.transform = 'translate(-50%,-50%) scale(1.05)';
                    const cancel_btn = document.querySelector("#cancel_btn");
                    cancel_btn.addEventListener("click", () => {
                        option_div.style.transform = 'translate(-50%,-50%) scale(0)';
                        option_div.innerHTML = "" ;
                    })
                })

            })