import {Component} from '@angular/core';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.scss']
})
export class FooterComponent {
  ngOnInit() {
    let path = window.location.href.substring(window.location.href.lastIndexOf('/') + 1);
    this.activateElement(path);
  }

  async activateElement(path: String) {
    let chat = document.getElementById("chat");
    let home = document.getElementById("home");
    let profile = document.getElementById("profile");
    chat?.addEventListener("click", () => this.activateElement("chat"));
    home?.addEventListener("click", () => this.activateElement("home"));
    profile?.addEventListener("click", () => this.activateElement("profil"));
    chat?.classList.remove("active");
    home?.classList.remove("active");
    profile?.classList.remove("active");
    switch (path) {
      case "chat":
        chat?.classList.add("active");
        break;
      case "home":
        home?.classList.add("active");
        break;
      case "profil":
        profile?.classList.add("active");
        break;
      default:
        break;
    }
  }
}
