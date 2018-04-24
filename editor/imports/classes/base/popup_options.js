import '/imports/classes/factories/create_popup_options_sprite';

PopupOptions = class PopupOptions {
  constructor (unit) {
    this.id = Math.random;
    this.unit = unit;
    this.sprite = createPopupOptionsSprite(this);
  }
}
