<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<html> 
<body>

    <table border="5px" bordercolor="black"  style="padding: 10px; color: navy;">
        <tr style="background-color: navy; color: white; text-align:center; font-size: 24px;"> 
            <th colspan="4"><xsl:value-of select="farmacia/@nombre"/></th>
        </tr>

        <tr style="background-color: lightblue; color: black; font-weight:bold; text-align:center; font-size: 20px;">
            <th>Nombre</th>
            <th>Via administración</th>
            <th>Contenido</th>
            <th>Precio</th>
        </tr>
        <xsl:for-each select="farmacia/medicamento">
            <!-- 1- ODENAR POR CATEGORIA -->
        
            <xsl:sort select="@categoria"/> 
            <tr>
                <td><xsl:value-of select="nombre"/></td>
                <td><xsl:value-of select="via_administracion"/></td>
                <td>
                    <xsl:value-of select="contenido"/>
                    <xsl:choose >
                        <xsl:when test="@categoria = 'Cápsula' ">
                            cápsulas
                        </xsl:when>
                        <xsl:when test="@categoria = 'Comprimido' ">
                            comprimidos
                        </xsl:when>
                        <xsl:otherwise >
                            ml
                        </xsl:otherwise>
                    </xsl:choose>
                </td>
                <td><xsl:value-of select="precio"/></td>
            </tr>
        

            <!-- 2- MAYORES DE 100 -->
            <!--         
            <xsl:if test="precio > 100 ">  
                <tr>
                    <td><xsl:value-of select="nombre"/></td>
                    <td><xsl:value-of select="via_administracion"/></td>
                    <td>
                        <xsl:value-of select="contenido"/>
                        <xsl:choose >
                            <xsl:when test="@categoria = 'Cápsula' ">
                                cápsulas
                            </xsl:when>
                            <xsl:when test="@categoria = 'Comprimido' ">
                                comprimidos
                            </xsl:when>
                            <xsl:otherwise >
                                ml
                            </xsl:otherwise>
                        </xsl:choose>
                    </td>
                    <td style="color:red"><xsl:value-of select="precio"/></td>
                </tr>
            </xsl:if>
            -->


            <!-- 3- CATEGORIA COMPRIMIDO O CAPSULA  -->
            <!--
            <xsl:sort select="nombre"/> 
            <xsl:choose> 
                <xsl:when test = "@categoria =  'Comprimido' "> 
                    <tr style="color:darkblue">
                        <td><xsl:value-of select="nombre"/></td>
                        <td><xsl:value-of select="via_administracion"/></td>
                        <td><xsl:value-of select="contenido"/>
                            <xsl:choose >
                                <xsl:when test="@categoria = 'Cápsula' ">
                                    cápsulas
                                </xsl:when>
                                <xsl:when test="@categoria = 'Comprimido' ">
                                    comprimidos
                                </xsl:when>
                                <xsl:otherwise >
                                    ml
                                </xsl:otherwise>
                            </xsl:choose>
                        </td>
                        <td><xsl:value-of select="precio"/></td>
                    </tr>
                </xsl:when> 		
                <xsl:when test = "@categoria = 'Cápsula' "> 
                    <tr style="color:darkgreen">
                        <td><xsl:value-of select="nombre"/></td>
                        <td><xsl:value-of select="via_administracion"/></td>
                        <td>
                            <xsl:value-of select="contenido"/>
                            <xsl:choose >
                                <xsl:when test="@categoria = 'Cápsula' ">
                                    cápsulas
                                </xsl:when>
                                <xsl:when test="@categoria = 'Comprimido' ">
                                    comprimidos
                                </xsl:when>
                                <xsl:otherwise >
                                    ml
                                </xsl:otherwise>
                            </xsl:choose>
                        </td>
                        <td ><xsl:value-of select="precio"/></td>
                    </tr>
                </xsl:when> 
            </xsl:choose>							
            -->
        </xsl:for-each>
    </table>
    
</body>
</html>
</xsl:template>
</xsl:stylesheet>