



        function loadDoc(){
          var xhttp = new XMLHttpRequest();
          xhttp.onreadystatechange = function() {
            if (this.status == 200) {
              document.getElementById("demo1").innerHTML = this.responseText;
            }
          };
          xhttp.open("POST", "{% url 'article:article_ticket' %}", true);
          xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
          xhttp.send("fname=ticket&lname=Gates");
        }
