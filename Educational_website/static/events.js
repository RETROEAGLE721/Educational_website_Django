let x=0;
        function events() { 
            x += 1;
            switch (x) {
                case 0:
                    {
                    break;
                    }
                case 1:
                    {
                    document.getElementById("demo1").style.visibility="visible";
                    document.getElementById("demo1").style.animation="ani 1s 1";
                    break;
                    }
                case 2:
                    {
                    document.getElementById("b1").style.visibility="visible";
                    document.getElementById("b2").style.visibility="visible";
                    document.getElementById("b1").style.animation="ani 1s 1";
                    document.getElementById("b2").style.animation="ani 1s 1";
                    break;
                    }
                    case 3:
                    {
                      document.getElementById("demo3").style.visibility="visible";
                    document.getElementById("demo3").style.animation="ani 1s 1";
                    break;
                    }
                    case 4:
                    {
                      document.getElementById("b3").style.visibility="visible";
                      document.getElementById("b4").style.visibility="visible";
                    document.getElementById("b3").style.animation="ani 1s 1";
                    document.getElementById("b4").style.animation="ani 1s 1";
                    break;
                    }
                    case 5:
                    {
                      document.getElementById("b5").style.visibility="visible";
                      document.getElementById("b6").style.visibility="visible";
                    document.getElementById("b5").style.animation="ani 1s 1";
                    document.getElementById("b6").style.animation="ani 1s 1";
                    break;
                    }
                    case 6:
                    {
                    document.getElementById("sub1").style.visibility="visible";
                    document.getElementById("sub1").style.animation="ani 1s 1";
                    break;
                    }
                  }
                }