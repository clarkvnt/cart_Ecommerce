<mxfile host="app.diagrams.net">
  <diagram name="Ecommerce DFD" id="ecommerce-dfd-1">
    <mxGraphModel dx="1000" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <!-- User -->
        <mxCell id="2" value="User" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;" vertex="1" parent="1">
          <mxGeometry x="60" y="180" width="80" height="80" as="geometry" />
        </mxCell>
        <!-- Web Front-End -->
        <mxCell id="3" value="Web Front-End" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="200" y="180" width="120" height="80" as="geometry" />
        </mxCell>
        <!-- Django Views -->
        <mxCell id="4" value="Django Views" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="370" y="180" width="120" height="80" as="geometry" />
        </mxCell>
        <!-- Database -->
        <mxCell id="5" value="Database" style="shape=cylinder;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="540" y="140" width="80" height="80" as="geometry" />
        </mxCell>
        <!-- Media Storage -->
        <mxCell id="6" value="Media Storage" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="540" y="240" width="100" height="60" as="geometry" />
        </mxCell>
        <!-- Authentication -->
        <mxCell id="7" value="Authentication" style="rounded=1;whiteSpace=wrap;html=1;dashed=1;strokeColor=#0070C0;" vertex="1" parent="1">
          <mxGeometry x="370" y="80" width="120" height="60" as="geometry" />
        </mxCell>
        <!-- Admin Access -->
        <mxCell id="8" value="Admin Access" style="rounded=1;whiteSpace=wrap;html=1;dashed=1;strokeColor=#FF0000;" vertex="1" parent="1">
          <mxGeometry x="370" y="300" width="120" height="60" as="geometry" />
        </mxCell>
        <!-- Flows -->
        <mxCell id="9" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;html=1;" edge="1" parent="1" source="2" target="3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="10" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;html=1;" edge="1" parent="1" source="3" target="4">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="11" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;html=1;" edge="1" parent="1" source="4" target="5">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="12" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;html=1;" edge="1" parent="1" source="4" target="6">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="13" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;dashed=1;strokeColor=#0070C0;html=1;" edge="1" parent="1" source="3" target="7">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="14" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;dashed=1;strokeColor=#FF0000;html=1;" edge="1" parent="1" source="3" target="8">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile> 