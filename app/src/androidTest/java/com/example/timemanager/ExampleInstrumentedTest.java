package com.example.timemanager;

import android.content.Context;

import androidx.test.platform.app.InstrumentationRegistry;
import androidx.test.ext.junit.runners.AndroidJUnit4;

import org.junit.Test;
import org.junit.runner.RunWith;

import static org.junit.Assert.*;

/**
 * Instrumented test, which will execute on an Android device.
<<<<<<< HEAD
 *LIJIAQi
 *LIJIAQi
 *LIJIAQi
 *LIJIAQi
 *LIJIAQi
 *LIJIAQi
 * LIJIAQi
=======
 *LIJIAQIDAOCIYIYOULIJIAQIDAOCIYIYOULIJIAQIDAOCIYIYOULIJIAQIDAOCIYIYOU
>>>>>>> eef970c6f540eb9eeabdcdfdd9ba61c13bfb3dca
 * @see <a href="http://d.android.com/tools/testing">Testing documentation</a>
 */
@RunWith(AndroidJUnit4.class)
public class ExampleInstrumentedTest {
    @Test
    public void useAppContext() {
        // Context of the app under test.
        Context appContext = InstrumentationRegistry.getInstrumentation().getTargetContext();
        assertEquals("com.example.timemanager", appContext.getPackageName());
    }
}