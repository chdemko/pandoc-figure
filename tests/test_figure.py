import io
import json
import textwrap

from unittest import TestCase

from panflute import Doc, convert_text, dump, debug

import pandoc_figure


class FigureTest(TestCase):
    def test_figure(self):
        definition = """\
            ::: {.figure caption="Figure caption" #fig:id}
            
            ![First subfigure](sub-figure-1.png "Title 1")
            
            ![Second subfigure](sub-figure-2.png "Title 2"){#fig:subfig2}
            
            :::
        """
        debug(textwrap.dedent(definition).strip())
        doc = convert_text(textwrap.dedent(definition).strip(), standalone=True)
        modified = pandoc_figure.main(doc)
        with io.StringIO() as stream:
            dump(modified, stream)
            contents = stream.getvalue()
            parsed = json.loads(contents)
            self.assertEqual(
                json.dumps(parsed["blocks"], indent=2),
                textwrap.dedent(
                    """
                    [
                      {
                        "t": "Figure",
                        "c": [
                          [
                            "fig:id",
                            [],
                            []
                          ],
                          [
                            null,
                            [
                              {
                                "t": "Plain",
                                "c": [
                                  {
                                    "t": "Str",
                                    "c": "Figure"
                                  },
                                  {
                                    "t": "Space"
                                  },
                                  {
                                    "t": "Str",
                                    "c": "caption"
                                  }
                                ]
                              }
                            ]
                          ],
                          [
                            {
                              "t": "Figure",
                              "c": [
                                [
                                  "",
                                  [],
                                  []
                                ],
                                [
                                  null,
                                  [
                                    {
                                      "t": "Plain",
                                      "c": [
                                        {
                                          "t": "Str",
                                          "c": "First"
                                        },
                                        {
                                          "t": "Space"
                                        },
                                        {
                                          "t": "Str",
                                          "c": "subfigure"
                                        }
                                      ]
                                    }
                                  ]
                                ],
                                [
                                  {
                                    "t": "Plain",
                                    "c": [
                                      {
                                        "t": "Image",
                                        "c": [
                                          [
                                            "",
                                            [],
                                            []
                                          ],
                                          [
                                            {
                                              "t": "Str",
                                              "c": "First"
                                            },
                                            {
                                              "t": "Space"
                                            },
                                            {
                                              "t": "Str",
                                              "c": "subfigure"
                                            }
                                          ],
                                          [
                                            "sub-figure-1.png",
                                            "Title 1"
                                          ]
                                        ]
                                      }
                                    ]
                                  }
                                ]
                              ]
                            },
                            {
                              "t": "Figure",
                              "c": [
                                [
                                  "fig:subfig2",
                                  [],
                                  []
                                ],
                                [
                                  null,
                                  [
                                    {
                                      "t": "Plain",
                                      "c": [
                                        {
                                          "t": "Str",
                                          "c": "Second"
                                        },
                                        {
                                          "t": "Space"
                                        },
                                        {
                                          "t": "Str",
                                          "c": "subfigure"
                                        }
                                      ]
                                    }
                                  ]
                                ],
                                [
                                  {
                                    "t": "Plain",
                                    "c": [
                                      {
                                        "t": "Image",
                                        "c": [
                                          [
                                            "",
                                            [],
                                            []
                                          ],
                                          [
                                            {
                                              "t": "Str",
                                              "c": "Second"
                                            },
                                            {
                                              "t": "Space"
                                            },
                                            {
                                              "t": "Str",
                                              "c": "subfigure"
                                            }
                                          ],
                                          [
                                            "sub-figure-2.png",
                                            "Title 2"
                                          ]
                                        ]
                                      }
                                    ]
                                  }
                                ]
                              ]
                            }
                          ]
                        ]
                      }
                    ]
                    """
                ).strip(),
            )
