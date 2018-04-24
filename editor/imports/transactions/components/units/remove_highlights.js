removeHighlights = (input) => {
  highlights = input.unit.highlights;
  highlights.forEach(function (element) {
    element.destroy();
  });
  input.unit.highlights = [];
  return new Right(input);
}

