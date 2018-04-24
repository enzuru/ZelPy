import '/imports/classes/base/popup_options';

popupOptions = (input) => {
  input.unit.popupOptions = new PopupOptions(input.unit);

  return new Right(input);
}
